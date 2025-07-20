from src.agent import agent

def main():
    print("LLM Hybrid Agent (Ollama + OpenAI)")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            print("Goodbye!")
            break
        result = agent.run(query)
        print(f"Agent: {result}\n")

if __name__ == "__main__":
    main()
