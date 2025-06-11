from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

JUDGMENT_PROMPT = """
You are a quality-checking observer agent reviewing another agent's work.

You are given:
- A scratchpad (the agent's internal thoughts)
- A final output (structured summary or report)

Evaluate:
1. Does the final output logically follow the scratchpad?
2. Are the conclusions consistent with the scratchpad?
3. Any signs of hallucination or conflicting logic?

Respond in this format:

JUDGMENT: PASS / NEEDS FIX / FLAGGED
REASON: <short explanation>

---

Scratchpad:
{scratchpad}

Final Output:
{output}
"""

prompt = ChatPromptTemplate.from_template(JUDGMENT_PROMPT)

def run_observer(scratchpad: str, output: str) -> str:
    return (prompt | llm).invoke({
        "scratchpad": scratchpad,
        "output": output
    }).content.strip()

