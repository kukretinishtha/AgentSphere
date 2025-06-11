# AgentSphere
Building a multi-agent research assistant capable of autonomously researching complex topics

```bash

AgentSphere/
│
├── agents/                        # Each agent's logic
│   ├── planner.py                 # Task decomposition
│   ├── researcher.py              # Web search via DuckDuckGo
│   ├── analyzer.py                # Analysis with scratchpad
│   ├── writer.py                  # Structured report writing
│   └── observer.py               # Quality judge for outputs
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
