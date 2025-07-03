import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(
        model=f"openai/{os.environ.get('MODEL_RUNNER_CHAT_MODEL')}",
        api_base=os.environ.get("MODEL_RUNNER_BASE_URL"),
        api_key="tada",
    ),
    name=f"{os.environ.get('AGENT_NAME')}",
    description=f"{os.environ.get('AGENT_DESCRIPTION')}",
    instruction=f"{os.environ.get('AGENT_INSTRUCTION')}",
)

