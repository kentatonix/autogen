import json
from pathlib import Path

import autogen
from autogen import AssistantAgent, Cache, UserProxyAgent

json_open = open("./config_list.json")
config_list = json.load(json_open)
llm_config = {
    "config_list": config_list,
    "cache_seed": None,  # Turns off caching, useful for testing different models
}


script_name = Path(__file__).stem
work_dir = Path("coding/" + script_name)
work_dir.mkdir(exist_ok=True)
work_dir_str = str(work_dir)

# # Start logging with logger_type and the filename to log to
# logging_session_id = autogen.runtime_logging.start(
#     logger_type="file", config={"filename": script_name + "_runtime.log"}
# )
# print("Logging session ID: " + str(logging_session_id))

# Start logging
logging_session_id = autogen.runtime_logging.start(config={"dbname": "autogen_logs/" + script_name + "_logs.db"})
print("Logging session ID: " + str(logging_session_id))

code_executor = autogen.coding.DockerCommandLineCodeExecutor(
    image="python:3.12-slim_proxy",
    work_dir="/home/autogen/autogen/apps/coding/cod",
    bind_dir="/home/naito/docker-compose_autogen/coding/cod",
    timeout=600,
    auto_remove=False,
)

assistant = AssistantAgent("assistant", llm_config=llm_config)
user_proxy = UserProxyAgent(
    "user_proxy", human_input_mode="NEVER", llm_config=False, code_execution_config={"executor": code_executor}
)

user_proxy.initiate_chat(
    assistant,
    message="/workspace/xrd.txtはXRDのスペクトルデータです。ピークマッチング法を使ってこの結晶は何か調べてください。",
)

autogen.runtime_logging.stop()
