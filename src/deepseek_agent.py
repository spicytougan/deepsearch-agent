import asyncio
from tools.github_tools import GitHubTool
from workflows.research_workflow import research_workflow

class DeepSeekAgent:
    def __init__(self, llm_api_key: str):
        self.llm_api_key = llm_api_key
        self.tools = {}
        self.workflows = {}
        
    def register_tool(self, tool_name: str, tool_func: callable):
        """Register a new MCP-compatible tool"""
        self.tools[tool_name] = tool_func
        
    def workflow(self, workflow_func: callable):
        """Decorator to register workflows"""
        self.workflows[workflow_func.__name__] = workflow_func
        return workflow_func
        
    async def execute_workflow(self, workflow_name: str, *args):
        """Execute a registered workflow"""
        if workflow_name not in self.workflows:
            raise ValueError(f"Workflow {workflow_name} not found")
        return await self.workflows[workflow_name](self, *args)
        
    async def call_llm(self, prompt: str):
        """Call LLM API with prompt"""
        # In a real implementation, this would call an actual LLM API
        # For demonstration, we'll simulate responses
        if "search query" in prompt:
            return "1. llm agents framework\n2. mcp tools integration\n3. deepsearch implementation"
        return f"LLM response to: {prompt}"
        
    async def run_tool(self, tool_name: str, params: dict):
        """Execute a registered tool"""
        if tool_name not in self.tools:
            raise ValueError(f"Tool {tool_name} not found")
        return await self.tools[tool_name](**params)

# Create agent instance
agent = DeepSeekAgent(llm_api_key="your-api-key")

# Register GitHub tool
gh_tool = GitHubTool(access_token="your-github-token")
agent.register_tool("github_search", gh_tool.search_repositories)

# Register workflow
agent.workflow(research_workflow)

# Example execution
async def main():
    print("DeepSeek Agent initialized")
    
    # Execute research workflow
    result = await agent.execute_workflow(
        "research_workflow", 
        "LLM agents with MCP tools integration"
    )
    
    # Print results
    print("\nResearch Results:")
    print(f"Topic: {result['topic']}")
    for query, repos in result['results'].items():
        print(f"\nQuery: {query}")
        for i, repo in enumerate(repos[:3], 1):  # Show top 3 results
            print(f"  {i}. {repo['full_name']} - Stars: {repo['stars']}")

if __name__ == "__main__":
    asyncio.run(main())