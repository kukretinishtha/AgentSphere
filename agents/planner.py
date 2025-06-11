from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

PLANNER_TEMPLATE = """
You are an expert planner. Decompose the user query into 2–4 detailed subtasks that can be passed to specialized agents. 
Be explicit, concise, and do not answer the query yourself.

Query: {query}
"""

prompt = ChatPromptTemplate.from_template(PLANNER_TEMPLATE)

def get_planner_chain() -> Runnable:
    return prompt | llm
