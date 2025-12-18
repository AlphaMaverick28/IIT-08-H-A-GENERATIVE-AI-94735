from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# load environment variables from .env
load_dotenv()

# create Groq LLM (VALID model for Groq)
llm = ChatGroq(
    model="llama3-8b-8192",
    api_key=os.getenv("GROQ_API_KEY")
)

# user input
user_input = input("You: ")

# stream response
for chunk in llm.stream(user_input):
    print(chunk.content, end="")
