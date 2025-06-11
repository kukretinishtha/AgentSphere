import uuid

# Global in-memory storage
conversation_history = {}

def create_new_session():
    session_id = str(uuid.uuid4())
    conversation_history[session_id] = {
        "logs": []
    }
    return session_id

def update_session(session_id, key, value):
    if session_id in conversation_history:
        conversation_history[session_id][key] = value
    else:
        raise ValueError("Session not found.")

def log_agent_step(session_id, agent_name, output):
    if session_id in conversation_history:
        conversation_history[session_id]["logs"].append({
            "agent": agent_name,
            "output": output
        })
