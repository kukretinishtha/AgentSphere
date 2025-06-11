import streamlit as st
import requests
import sys, os

# Allow importing from project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

BASE_URL = "http://localhost:8000"

st.title("🧠 Multi-Agent Research Assistant")

if "session_id" not in st.session_state:
    st.session_state.session_id = None

query = st.text_area("Enter your research query", height=100)
submit = st.button("Submit")

if submit and query:
    with st.spinner("Agents are working..."):
        response = requests.post(f"{BASE_URL}/submit_query", json={"query": query})
        data = response.json()
        st.session_state.session_id = data["session_id"]
        st.success("Query submitted!")

if st.session_state.session_id:
    st.markdown(f"**Session ID:** `{st.session_state.session_id}`")

    if st.button("🔍 Refresh Results"):
        hist = requests.get(f"{BASE_URL}/get_history/{st.session_state.session_id}").json()

        # Agent Logs
        st.subheader("🧩 Agent Logs")
        for step in hist.get("logs", []):
            st.markdown(f"**🛠️ {step['agent']} Output:**")
            st.code(step["output"] if isinstance(step["output"], str) else str(step["output"]))

        # Analyzer Scratchpad
        if "analyzer_scratchpad" in hist:
            st.subheader("🧠 Analyzer Scratchpad")
            st.code(hist["analyzer_scratchpad"])

        # Observer
        if "analyzer_judgment" in hist:
            st.subheader("🔍 Observer Judgment")
            st.warning(hist["analyzer_judgment"])

        # Final Report
        if "final_report" in hist:
            st.subheader("📄 Final Report")
            st.markdown(hist["final_report"])

            st.download_button(
                label="📥 Download Markdown",
                data=hist["final_report"],
                file_name="final_report.md",
                mime="text/markdown"
            )

