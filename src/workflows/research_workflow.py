import asyncio

async def research_workflow(agent, topic: str):
    """Research workflow using LLM and GitHub tools"""
    # Step 1: Use LLM to generate search queries
    prompt = f"Generate 3 GitHub search queries for researching: {topic}"
    queries_response = await agent.call_llm(prompt)
    
    # Parse queries from LLM response
    queries = [q.strip() for q in queries_response.split('\n') if q.strip()]
    print(f"Generated queries: {queries}")
    
    # Step 2: Execute searches
    results = {}
    for query in queries:
        try:
            search_results = await agent.run_tool(
                "github_search", 
                {"query": query}
            )
            results[query] = search_results
            print(f"Found {len(search_results)} results for '{query}'")
        except Exception as e:
            print(f"Error searching for '{query}': {str(e)}")
            results[query] = []
    
    # Step 3: Return aggregated results
    return {
        "topic": topic,
        "queries": queries,
        "results": results
    }