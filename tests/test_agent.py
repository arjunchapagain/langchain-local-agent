from src.agent import agent

def test_agent_response():
    response = agent.run("What is 2 + 2?")
    assert isinstance(response, str)
    assert "4" in response or "four" in response.lower())
