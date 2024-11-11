import json
import pprint
from pathlib import Path

from pandas import read_json

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
    work_dir="/home/autogen/autogen/apps/coding/stockprice",
    bind_dir="/home/naito/docker-compose_autogen/coding/stockprice",
    timeout=600,
    auto_remove=False,
)


assistant = AssistantAgent("assistant", llm_config=llm_config, max_consecutive_auto_reply=2)
user_proxy = UserProxyAgent(
    "user_proxy", human_input_mode="NEVER", llm_config=False, code_execution_config={"executor": code_executor}
)
with Cache.redis(redis_url="redis://redis:6379/0") as cache:
    user_proxy.initiate_chat(
        assistant,
        message="NVDAとTESLAの株価のYTD変化をプロットしてください。プロットをplot.pngというファイルに保存してください。",
        clear_history=False,
        cache=cache,
    )

chat_messages = assistant.chat_messages

assistant2 = AssistantAgent(
    "assistant", llm_config=llm_config, max_consecutive_auto_reply=2, chat_messages=chat_messages
)
user_proxy2 = UserProxyAgent(
    "user_proxy", human_input_mode="NEVER", llm_config=False, code_execution_config={"executor": code_executor}
)
with Cache.redis(redis_url="redis://redis:6379/0") as cache:
    user_proxy.initiate_chat(
        assistant2,
        message="先ほど作成したファイルの名前を教えて",
        clear_history=False,
        cache=cache,
    )

autogen.runtime_logging.stop()
print(user_proxy.chat_messages)
# 1. Convert defaultdict to a normal dictionary with lists
# For simplicity, we'll iterate through and structure it for JSON compatibility.
formatted_chat_messages = {
    str(agent): messages  # Convert agent object to string key for JSON compatibility
    for agent, messages in user_proxy.chat_messages.items()
}

# 2. Save as JSON
with open("chat_messages.json", "w", encoding="utf-8") as json_file:
    json.dump(formatted_chat_messages, json_file, ensure_ascii=False, indent=4)

print("Chat messages have been saved to chat_messages.json")
