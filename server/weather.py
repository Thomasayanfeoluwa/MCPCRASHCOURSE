from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

# Contants
NWS_API_BASE = ""
USER_AGENT = "weather-app/1.0"