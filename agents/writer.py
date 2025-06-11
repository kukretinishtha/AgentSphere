from langchain_openai import ChatOpenAI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

WRITER_TEMPLATE = """
You are a technical business writer. Write a detailed report from the analysis provided below.
Make it well-structured with headings, and cite information where appropriate. Be concise and factual.

Analysis:
{analyzed_data}
"""

prompt = ChatPromptTemplate.from_template(WRITER_TEMPLATE)

def get_writer_chain() -> Runnable:
    return prompt | llm
