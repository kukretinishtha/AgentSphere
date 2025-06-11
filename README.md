# 📘 AgentSphere – Multi-Agent Research Assistant

AgentSphere is a LangGraph-powered research assistant that uses multiple AI agents to collaboratively analyze and report on complex topics. It supports real-time research using DuckDuckGo, chain-of-thought analysis, scratchpad reasoning, and observer-based validation for trustworthy outputs.

## 🌐 Live Features
```bash
🧠 Planner Agent: Decomposes the user’s query into subtasks.
🌍 Researcher Agent: Searches the web using DuckDuckGo.
🔍 Analyzer Agent: Synthesizes findings using a scratchpad.
🕵️ Observer Agent: Judges analysis for hallucination or error.
✍️ Writer Agent: Produces a clean, structured report.
📜 Streamlit UI: User-friendly frontend for interaction.
🔁 Conversation Memory: Stores session history in-memory.
🚀 Quickstart
```

## How to setup on local
✅ 1. Clone the Repo
```bash
git clone https://github.com/yourusername/AgentSphere.git
cd AgentSphere
```

✅ 2. Install Dependencies
```bash
Use Python 3.12.1 or higher.
pip install -r requirements.txt
```
✅ 3. Add Your .env File

Create a .env file in the root:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

## 🧪 How to Run
▶️ Run the Backend (FastAPI)
```bash
uvicorn api.main:app --reload
```
Docs available at: http://localhost:8000/docs

▶️ Run the Frontend (Streamlit)
```bash
streamlit run ui/app.py
```
Available at: http://localhost:8501

## 🧠 Sample Flow (UI/Logs)

User submits a query:
“What are the business and technical implications of AI agents in enterprise?”
Agents collaborate to produce:
Subtasks (Planner)
Search results (Researcher)
Scratchpad + Summary (Analyzer)
Observer judgment (PASS / NEEDS FIX)
Final Markdown report (Writer)

## 🧱 Folder Structure
```bash

AgentSphere/
│
├── agents/                        # Each agent's logic
│   ├── planner.py                 # Task decomposition
│   ├── researcher.py              # Web search via DuckDuckGo
│   ├── analyzer.py                # Analysis with scratchpad
│   ├── writer.py                  # Structured report writing
│   └── observer.py                # Quality judge for outputs
│
├── api/                           # FastAPI server
│   └── main.py                    # Submit query / get results / monitor
│
├── core/                          # System pipeline + memory
│   ├── langgraph_flow.py          # LangGraph multi-agent DAG
│   ├── memory_store.py            # In-memory session storage
│   └── utils.py                   # (Optional) helpers/loggers
│
├── ui/                            # Streamlit-based frontend
│   └── app.py                     # Run: `streamlit run ui/app.py`
│
├── docs/                          # Documentation
│   └── architecture.png           # Diagram of the system
│
├── .env                           # OpenAI API key (add to .gitignore)
├── .gitignore                     # Ignore .env, __pycache__, etc.
├── requirements.txt               # All dependencies
├── Dockerfile                     # Docker image setup
├── docker-compose.yml             # Orchestration
├── README.md                      # Project overview and usage
└── LICENSE                        # (Optional) open-source license

```
## 🛠️ Tech Stack
LLMs: OpenAI GPT-4o / 3.5
Orchestration: LangGraph + LangChain
Search: DuckDuckGo
Frontend: Streamlit
Backend: FastAPI
Memory: Python In-Memory Dict

## 📥 API Endpoints
#### route
/submit_query	
Method : POST	
Description : Submit user query

#### route
/get_history/{session_id}	
Method : GET	
Description : Get full agent conversation

### route
/monitor/{session_id}	
Method: GET	
Description: View agent progress (status)