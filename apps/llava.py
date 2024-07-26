import autogen
from autogen import Agent, AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.llava_agent import LLaVAAgent, llava_call

llava_config_list = [
    {
        "model": "ollama/llava:7b-v1.6-mistral-q6_K",
        "api_key": "None",
        "base_url": "http://llm:4000",
    }
]

rst = llava_call(
    "What's the breed of this dog? file is <img /home/autogen/autogen/apps/images/dog.jfif>",
    llm_config={"config_list": llava_config_list, "temperature": 0},
)

print(rst)
