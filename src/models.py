import os
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")


def get_llm():
    if USE_OPENAI:
        return ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    else:
        return Ollama(
            model=OLLAMA_MODEL,
            temperature=0
        )
