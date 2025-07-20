LLM Hybrid Agent: Local Ollama + OpenAI API Integration

A Python project that integrates a local LLM (via Ollama) with the OpenAI API, using LangChain to enable tool use, internet access, and hybrid agent capabilities.

---

## Features

- Use Ollama models like LLaMA3 or DeepSeek locally
- Add internet search with DuckDuckGo tool
- Switch between local and cloud models dynamically
- Powered by LangChain for agent capabilities
- Easily extendable with custom tools or retrieval (RAG)

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/arjunchapagain/Arjun-LLM-Agent.git
cd Arjun-LLM-Agent
```

### 2. Set up environment

#### Option A: With Conda

```bash
conda create -n langchain-llm python=3.11
conda activate langchain-llm
```

#### Option B: With venv

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup API Key (for OpenAI)

Create a `.env` file or export your key:

```bash
export OPENAI_API_KEY="your-openai-api-key"
```

Or create a `.env` file:

```env
OPENAI_API_KEY=your-openai-api-key
```

---

## Run the Agent

```bash
python main.py
```

Or test it directly:

```bash
python -m src.agent
```

---

## Project Structure

```
Arjun-LLM-Agent/
├── .github/workflows/lint.yml     # Optional GitHub Actions
├── src/
│   ├── agent.py                   # Main LangChain agent
│   ├── models.py                  # Local/OpenAI LLMs
│   └── tools.py                   # Internet Search tool
├── tests/
│   └── test_agent.py              # Basic test
├── main.py                        # Entry point
├── .env.example                   # Env variable template
├── .gitignore
├── LICENSE                        # MIT License
├── requirements.txt
└── README.md
```

---

## How It Works

### LLMs
- Local: Uses Ollama (e.g., `llama3`, `deepseek-coder`)
- Cloud: Uses OpenAI (`gpt-4o`, `gpt-3.5-turbo`) if fallback enabled

### Internet Tool
Integrated with DuckDuckGo via LangChain:

```python
from langchain_community.tools import DuckDuckGoSearchRun
```

---

## Example Usage

```python
from src.agent import agent

question = "What's the latest AI news?"
print(agent.run(question))
```

---

## Notes

- Keep your OpenAI key secure
- Local LLMs preferred for privacy; cloud use is optional
- Easily extendable with:
  - File summarization
  - RAG tools
  - External APIs

---

## License

MIT License © 2025 Arjun Chapagain

---

## Author

Created by Arjun Chapagain

---
