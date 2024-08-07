import autogen
from autogen import Agent, AssistantAgent, ConversableAgent, UserProxyAgent
from autogen.agentchat.contrib.llava_agent import LLaVAAgent, llava_call

llava_config_list = [{"model": "llava:34b-v1.6-q8_0", "api_key": "None", "base_url": "http://llm:11434/api/generate"}]

rst = llava_call(
    "What's the breed of this dog? file is <img /home/autogen/autogen/apps/images/dog.jfif>",
    llm_config={"config_list": llava_config_list, "temperature": 0},
)

print(rst)
