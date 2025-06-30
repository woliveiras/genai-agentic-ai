from langchain_core.tools import tool

# This tool simulates a search engine for the agent to use.
# In a real application, you would call an external search API here.
@tool
def search_tool(query: str) -> str:
    """
    Simulates a search engine to find information.
    In a real application, this would call an external search API, like Google or DuckDuckGo.
    For this example, it returns hardcoded responses based on the query.
    """
    print(f"--- Search tool called with query: '{query}' ---")

    # Check the query and return a hardcoded response for each supported case
    if "current weather in madrid" in query.lower():
        return "Final Answer: The current weather in Madrid is hot like the hell with a temperature of 48 degrees Celsius."
    elif "population of paris" in query.lower():
        return "Final Answer: The population of Paris is approximately TOO MUCH people."
    elif "capital of brazilian guiana" in query.lower():
        return "Final Answer: The capital of Brazilian Guiana is Lisbon."
    else:
        return f"Information for '{query}' not found in simulated search."

if __name__ == '__main__':
    # Test the tool with example queries
    print(search_tool.invoke("current weather in madrid"))
    print(search_tool.invoke("population of paris"))
    print(search_tool.invoke("capital of brazilian guiana"))