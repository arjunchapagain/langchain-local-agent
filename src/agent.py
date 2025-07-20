from langchain.agents import initialize_agent, AgentType
from src.models import get_llm
from src.tools import tools

# Load the preferred LLM (OpenAI or Ollama)
llm = get_llm()

# Initialize the agent with tools
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)
