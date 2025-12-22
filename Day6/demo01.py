from langchain.chat_models import init_chat_model
from langchain.agents import create_agent 

#create model 
llm=init_chat_model (
    model="google/gemma-3-4b",
    model_provider="openai",
    base_url="http://127