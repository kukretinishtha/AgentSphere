from fastapi import FastAPI
from pydantic import BaseModel

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from core.langgraph_flow import agent_graph
from core.memory_store import create_new_session, conversation_history

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/submit_query")
def submit_query(req: QueryRequest):
    session_id = create_new_session()
    state = {"query": req.query}
    graph = agent_graph(session_id)
    result = graph.invoke(state)
    conversation_history[session_id]["query"] = req.query
    print(result)
    return {
        "session_id": session_id,
        "result": result
    }

@app.get("/get_history/{session_id}")
def get_history(session_id: str):
    return conversation_history.get(session_id, {"error": "Session not found"})


@app.get("/monitor/{session_id}")
def monitor(session_id: str):
    session = conversation_history.get(session_id, {})
    logs = session.get("logs", [])
    status = "Pending"
    if "final_report" in session:
        status = "Complete"
    elif any(log['agent'] == "Writer" for log in logs):
        status = "Writing"
    elif any(log['agent'] == "Analyzer" for log in logs):
        status = "Analyzing"
    elif any(log['agent'] == "Researcher" for log in logs):
        status = "Researching"
    elif any(log['agent'] == "Planner" for log in logs):
        status = "Planning"
    
    return {
        "session_id": session_id,
        "status": status,
        "steps_completed": [log['agent'] for log in logs]
    }
