from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

# Load environment variables
load_dotenv()

# Validate required API keys
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY is missing!")

if not os.getenv("LANGCHAIN_API_KEY"):
    raise ValueError("LANGCHAIN_API_KEY is missing!")

# Create the LangChain model
llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0.7
)

# Get user input
user_prompt = input("Enter your prompt: ")

# Send prompt through LangChain
response = llm.invoke(user_prompt)

# Display the response
print("\nAI Response:\n")
print(response.content)