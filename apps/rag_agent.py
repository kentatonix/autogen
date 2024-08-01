import json
import os
from pathlib import Path

import chromadb

import autogen
from autogen.agentchat.contrib.retrieve_assistant_agent import RetrieveAssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent

# Accepted file formats for that can be stored in
# a vector database instance
from autogen.retrieve_utils import TEXT_FORMATS

json_open = open("./config_list.json")
config_list_json = json.load(json_open)
llm_config = {
    "config_list": config_list_json["config_list"],
    "cache_seed": None,  # Turns off caching, useful for testing different models
}

# 1. create an RetrieveAssistantAgent instance named "assistant"
assistant = RetrieveAssistantAgent(
    name="assistant", system_message="You are a helpful assistant.", llm_config=llm_config
)

# 2. create the RetrieveUserProxyAgent instance named "ragproxyagent"
# By default, the human_input_mode is "ALWAYS", which means the agent will ask for human input at every step. We set it to "NEVER" here.
# `docs_path` is the path to the docs directory. It can also be the path to a single file, or the url to a single file. By default,
# it is set to None, which works only if the collection is already created.
# `task` indicates the kind of task we're working on. In this example, it's a `code` task.
# `chunk_token_size` is the chunk token size for the retrieve chat. By default, it is set to `max_tokens * 0.6`, here we set it to 2000.
# `custom_text_types` is a list of file types to be processed. Default is `autogen.retrieve_utils.TEXT_FORMATS`.
# This only applies to files under the directories in `docs_path`. Explicitly included files and urls will be chunked regardless of their types.
# In this example, we set it to ["non-existent-type"] to only process markdown files. Since no "non-existent-type" files are included in the `websit/docs`,
# no files there will be processed. However, the explicitly included urls will still be processed.
print(os.path.join(os.path.abspath(""), "..", "website", "docs"))
ragproxyagent = RetrieveUserProxyAgent(
    name="ragproxyagent",
    human_input_mode="qa",
    max_consecutive_auto_reply=3,
    retrieve_config={
        "task": "default",
        "docs_path": [
            "/home/autogen/autogen/apps/2403.08299v1.pdf",
        ],
        "collection_name": "ragchat3",
        "custom_text_types": ["non-existent-type"],
        "chunk_token_size": 2000,
        # "model": llm_config["config_list"][0]["model"],
        "vector_db": "chroma",  # to use the deprecated `client` parameter, set to None and uncomment the line above
        "embedding_model": "all-mpnet-base-v2",
        "must_break_at_empty_line": False,
        "get_or_create": True,
        "overwrite": False,  # set to True if you want to overwrite an existing collection
    },
    code_execution_config=False,  # set to False if you don't want to execute the code
)

# reset the assistant. Always reset the assistant before starting a new conversation.
assistant.reset()

# given a problem, we use the ragproxyagent to generate a prompt to be sent to the assistant as the initial message.
# the assistant receives the message and generates a response. The response will be sent back to the ragproxyagent for processing.
# The conversation continues until the termination condition is met, in RetrieveChat, the termination condition when no human-in-loop is no code block detected.
# With human-in-loop, the conversation will continue until the user says "exit".
code_problem = "What is AutoDev"
chat_result = ragproxyagent.initiate_chat(
    assistant, message=ragproxyagent.message_generator, problem=code_problem, search_string="spark"
)  # search_string is used as an extra filter for the embeddings search, in this case, we only want to search documents that contain "spark".
