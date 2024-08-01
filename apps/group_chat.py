import json
from pathlib import Path

import autogen
from autogen import AssistantAgent, UserProxyAgent

json_open = open("./config_list.json")
config_list_json = json.load(json_open)
llm_config = {
    "config_list": config_list_json["config_list"],
    "cache_seed": None,  # Turns off caching, useful for testing different models
}


script_name = Path(__file__).stem
work_dir = Path("coding/" + script_name)
work_dir.mkdir(exist_ok=True)

# Start logging with logger_type and the filename to log to
logging_session_id = autogen.runtime_logging.start(
    logger_type="file", config={"filename": script_name + "_runtime.log"}
)
print("Logging session ID: " + str(logging_session_id))

with autogen.coding.DockerCommandLineCodeExecutor(
    image="python:3.12-slim_proxy",
    work_dir=work_dir,
    bind_dir="/home/naito/docker-compose_autogen/coding/" + script_name,
    timeout=600,
    auto_remove=False,
) as code_executor:

    initializer = autogen.UserProxyAgent(
        name="Init",
    )

    assistant = AssistantAgent(
        "assistant",
        llm_config=llm_config,
        system_message="""You are a helpful AI assistant.
Solve tasks using your coding and language skills.
In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
    1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
    2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
Reply "TERMINATE" in the end when everything is done.Please output everything in Japanese.
    """,
    )

    executor = UserProxyAgent("user_proxy", human_input_mode="NEVER", code_execution_config={"executor": code_executor})

    scientist = autogen.AssistantAgent(
        name="Research_Action_1",
        llm_config=llm_config,
        system_message="""You are the Scientist. Please categorize papers after seeing their abstracts printed and create a markdown table with Domain, Title, Authors, Summary and Link.Please output everything in Japanese.""",
    )

    groupchat = autogen.GroupChat(
        agents=[initializer, assistant, executor, scientist],
        messages=[],
        max_round=20,
    )

    manager = autogen.GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config,
        system_message="""Group chat manager.Please output everything in Japanese.""",
    )

    initializer.initiate_chat(
        manager,
        message="トピック: 先週の LLM アプリケーション論文。要件: さまざまな分野からの 5 ～ 10 件の論文。",
        clear_history=False,
        summary_method="reflection_with_llm",
    )

autogen.runtime_logging.stop()
