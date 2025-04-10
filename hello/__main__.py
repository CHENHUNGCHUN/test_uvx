from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import os, sys

# Initialize FastMCP server
mcp = FastMCP("hello")

print("PATH from Claude:", os.environ.get("PATH"), file=sys.stderr)

@mcp.tool()
def main():
    return "hello how are you"

# if __name__ == "__main__":
#     main()
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')