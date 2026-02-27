import os
from dotenv import load_dotenv

# Load environment variables first
load_dotenv()

# Get API key explicitly
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Check your .env file.")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate


# Explicitly pass API key
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=api_key,
    max_retries=3
)


prompt = PromptTemplate.from_template("""
You are a senior UI engineer.

Improve this Streamlit code using modern UI/UX principles:

- spacing
- typography
- colors
- layout alignment

Return full improved python code only.

Code:
{code}
""")


chain = prompt | llm


def refine_code(code: str) -> str:
    response = chain.invoke({"code": code})
    return response.content