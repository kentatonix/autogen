import json
from pathlib import Path

import autogen
from autogen import AssistantAgent, Cache, UserProxyAgent

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
    assistant = AssistantAgent("assistant", llm_config=llm_config)
    user_proxy = UserProxyAgent(
        "user_proxy", human_input_mode="NEVER", code_execution_config={"executor": code_executor}
    )

    # Use Redis as cache
    with Cache.redis(redis_url="redis://localhost:6379/0") as cache:
        user_proxy.initiate_chat(
            assistant,
            message="Plot a chart of NVDA and TESLA stock price change YTD. Save the plot to a file called plot.png",
        )

autogen.runtime_logging.stop()
