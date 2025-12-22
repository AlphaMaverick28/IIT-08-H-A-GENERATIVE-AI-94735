from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
# read API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY is not set")

# create Groq model (VALID Groq model)
llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=api_key
)

# chat loop
user_input = input("You: ")

for chunk in llm.stream(user_input):
    print(chunk.content, end="")
