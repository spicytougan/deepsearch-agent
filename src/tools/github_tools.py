import os
from github import Github

class GitHubTool:
    def __init__(self, access_token=None):
        """Initialize GitHub API client"""
        self.access_token = access_token or os.getenv('GITHUB_TOKEN')
        if not self.access_token:
            raise ValueError("GitHub access token not provided")
        self.client = Github(self.access_token)
        
    async def search_repositories(self, query: str):
        """Search GitHub repositories"""
        results = self.client.search_repositories(query)
        return [{
            "name": repo.name,
            "full_name": repo.full_name,
            "html_url": repo.html_url,
            "description": repo.description,
            "stars": repo.stargazers_count
        } for repo in results]
        
    async def get_file_contents(self, owner: str, repo: str, path: str, branch: str = "main"):
        """Get contents of a file from GitHub"""
        repo = self.client.get_repo(f"{owner}/{repo}")
        contents = repo.get_contents(path, ref=branch)
        return contents.decoded_content.decode("utf-8")