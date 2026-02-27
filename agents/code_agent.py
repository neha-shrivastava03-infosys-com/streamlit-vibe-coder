import os
from dotenv import load_dotenv

# Load environment variables FIRST
load_dotenv()

# Verify API key is loaded
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found!")

print("API KEY loaded:", api_key[:20], "...")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


# Initialize OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=api_key   # explicitly pass key (important)
)


# Prompt template
prompt = PromptTemplate.from_template("""
You are an expert Streamlit developer.

Generate modern, clean Streamlit UI code for:

{description}

Requirements:
- modern layout
- clean spacing
- professional styling
- return ONLY python code
""")


# Create pipeline
chain = prompt | llm


# Function used by app.py
def generate_code(description: str) -> str:
    response = chain.invoke({"description": description})
    return response.content