import json
from pathlib import Path

import autogen
from autogen import AssistantAgent, UserProxyAgent

local_llm_config = {
    "config_list": [
        {
            "model": "ollama/codellama:7b",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://llm:4000",  # Your LiteLLM URL
        }
    ],
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
    bind_dir="/home/naito/docker-compose_autogen/apps/coding/" + script_name,
    timeout=600,
    auto_remove=False,
) as code_executor:
    assistant = AssistantAgent("assistant", llm_config=local_llm_config)
    user_proxy = UserProxyAgent(
        "user_proxy", human_input_mode="NEVER", code_execution_config={"executor": code_executor}
    )

    # Start the chat
    user_proxy.initiate_chat(
        assistant,
        message="Plot a chart of NVDA and TESLA stock price change YTD. Save the plot to a file called plot.png",
    )

autogen.runtime_logging.stop()
