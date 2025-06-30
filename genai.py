import ollama

# This function sends a prompt to the Ollama LLM and returns a generated slogan.
def generate_slogan(topic: str) -> str:
    """
    Generates a marketing slogan for a given topic using Ollama.
    """
    # Prepare the prompt for the LLM
    prompt = f"Generate a catchy and concise marketing slogan for a company that specializes in {topic}. Make it sound innovative."
    # Call the Ollama LLM with the prompt and get the response
    response = ollama.chat(model='llama3', messages=[
        {'role': 'user', 'content': prompt}
    ])
    # Extract the generated slogan from the response
    return response['message']['content']

if __name__ == "__main__":
    print("--- Generative AI Example (Ollama) ---")
    # Example 1: Generate a slogan for retro gaming
    topic = "retro gaming and nostalgia"
    slogan = generate_slogan(topic)
    print(f"Topic: {topic}")
    print(f"Generated Slogan: {slogan}\n")

    # Example 2: Generate a slogan for board games
    topic_2 = "board games and tabletop gaming"
    slogan_2 = generate_slogan(topic_2)
    print(f"Topic: {topic_2}")
    print(f"Generated Slogan: {slogan_2}\n")