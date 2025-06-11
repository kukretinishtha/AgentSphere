from duckduckgo_search import DDGS
from typing import List, Dict

def search_web(query: str, max_results: int = 5) -> List[str]:
    """
    Search the web using DuckDuckGo and return a list of results (title + URL).
    """
    results = []
    with DDGS() as ddgs:
        search_results = ddgs.text(query, region='wt-wt', safesearch='Moderate', max_results=max_results)
        for result in search_results:
            title = result.get("title", "")
            href = result.get("href", "")
            snippet = result.get("body", "")
            results.append(f"{title} - {href}\nSnippet: {snippet}")
    return results


def batch_search(subtasks: List[str], max_results_per_subtask: int = 5) -> Dict[str, List[str]]:
    """
    Takes a list of subtasks and runs a web search for each.
    Returns a dictionary with subtask as key and list of search results as value.
    """
    aggregated = {}
    for task in subtasks:
        try:
            aggregated[task] = search_web(task, max_results=max_results_per_subtask)
        except Exception as e:
            aggregated[task] = [f"Search failed for: {task}. Error: {str(e)}"]
    return aggregated
