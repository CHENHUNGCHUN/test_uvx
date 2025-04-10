from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("hello")

@mcp.tool()
def main():
    return "hello how are you"

# if __name__ == "__main__":
#     main()
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')