import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

os.environ["OPENAI_API_KEY"] = "tada"
os.environ["OPENAI_API_BASE"] = f"{os.environ.get('DMR_BASE_URL')}/engines/llama.cpp/v1"

root_agent = Agent(
    model=LiteLlm(model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}"),
    name=f"{os.environ.get('AGENT_NAME')}",
    description=f"{os.environ.get('AGENT_DESCRIPTION')}",
    instruction=f"{os.environ.get('AGENT_INSTRUCTION')}",
)
