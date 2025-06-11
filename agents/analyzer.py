from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable

from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

ANALYZER_TEMPLATE = """
You are a critical-thinking analyst. Follow this process:

1. Read the findings.
2. Identify major themes and conflicting points.
3. Reflect in a scratchpad.
4. Then summarize in a structured output.

Findings:
{subtask_data}

---

**Scratchpad** (your thoughts before final summary):
"""

prompt = ChatPromptTemplate.from_template(ANALYZER_TEMPLATE)

def get_analyzer_chain() -> Runnable:
    return prompt | llm
