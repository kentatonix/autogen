import json
from pathlib import Path

from pandas import read_json

import autogen
from autogen import AssistantAgent, Cache, UserProxyAgent
from autogen.agentchat.contrib.capabilities.teachability import Teachability

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
    work_dir="/home/autogen/autogen/apps/coding/stockprice",
    bind_dir="/home/naito/docker-compose_autogen/coding/stockprice",
    timeout=600,
    auto_remove=False,
)

assistant = AssistantAgent("assistant", llm_config=llm_config)

# Instantiate the Teachability capability. Its parameters are all optional.
teachability = Teachability(
    verbosity=3,  # 0 for basic info, 1 to add memory operations, 2 for analyzer messages, 3 for memo lists.
    reset_db=False,
    path_to_db_dir="./teach_db/teachability_db",
    recall_threshold=1.5,  # Higher numbers allow more (but less relevant) memos to be recalled.
)

# Instantiate a UserProxyAgent to represent the user. But in this notebook, all user input will be simulated.
user = UserProxyAgent(name="user", human_input_mode="NEVER", code_execution_config={"executor": code_executor})

# Now add the Teachability capability to the agent.
teachability.add_to_agent(assistant)

text = "Plot a chart of NVDA and TESLA stock price change YTD. Save the plot to a file called plot.png"
user.initiate_chat(assistant, message=text, clear_history=True)

autogen.runtime_logging.stop()
