from langgraph.graph import StateGraph, END
from agents.planner import get_planner_chain
from agents.researcher import search_web
from agents.analyzer import get_analyzer_chain
from agents.writer import get_writer_chain
from agents.observer import run_observer
from core.memory_store import update_session, log_agent_step


from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict, Any

# Define the structure of the state passed between nodes
class AgentState(TypedDict):
    query: str
    subtasks: List[str]
    research_results: Dict[str, List[str]]
    analyzed_summary: str
    final_report: str

# Define the workflow using the state schema
def agent_graph(session_id):
    workflow = StateGraph(state_schema=AgentState) 

    def planner_fn(state):
        chain = get_planner_chain()
        result = chain.invoke({"query": state["query"]})
        subtasks = [task.strip() for task in result.content.split("\n") if task.strip()]
        update_session(session_id, "subtasks", subtasks)
        log_agent_step(session_id, "Planner", result.content)
        return {"subtasks": subtasks}

    def researcher_fn(state):
        subtasks = state.get("subtasks", [])
        results = {}
        for task in subtasks:
            if not task.strip():
                continue  # Skip empty subtasks

        update_session(session_id, "research_results", results)
        log_agent_step(session_id, "Researcher", results)
        return {"research_results": results}
    
    def analyzer_fn(state):
        research_results = state.get("research_results", {})
        flat_text = "\n".join(f"{k}: {v}" for k, v in research_results.items())
        
        chain = get_analyzer_chain()
        full_output = chain.invoke({"subtask_data": flat_text}).content

        # Separate scratchpad and summary
        scratchpad = full_output.split("**Scratchpad**")[-1].split("---")[0].strip()
        summary = full_output.split("---")[-1].strip()

        # Run Observer Judgment
        judgment = run_observer(scratchpad, summary)

        # Log & store in memory
        update_session(session_id, "analyzed_summary", summary)
        update_session(session_id, "analyzer_scratchpad", scratchpad)
        update_session(session_id, "analyzer_judgment", judgment)

        log_agent_step(session_id, "Analyzer", {
            "scratchpad": scratchpad,
            "summary": summary,
            "observer": judgment
        })

        return {"analyzed_summary": summary}


    def writer_fn(state):
        analysis = state.get("analyzed_summary", "")
        chain = get_writer_chain()
        report = chain.invoke({"analyzed_data": analysis}).content
        update_session(session_id, "final_report", report)
        log_agent_step(session_id, "Writer", report)
        return {"final_report": report}

    workflow.add_node("Planner", planner_fn)
    workflow.add_node("Researcher", researcher_fn)
    workflow.add_node("Analyzer", analyzer_fn)
    workflow.add_node("Writer", writer_fn)

    workflow.set_entry_point("Planner")
    workflow.add_edge("Planner", "Researcher")
    workflow.add_edge("Researcher", "Analyzer")
    workflow.add_edge("Analyzer", "Writer")
    workflow.add_edge("Writer", END)

    return workflow.compile()
