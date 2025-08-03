from server import mcp
from utils.file_reader import read_csv_summary, get_csv_headers, get_columnwise_content, get_rowwise_content
from utils.llm_processing import get_synopsis_of_csv_content

@mcp.tool()
def summarize_csv(filename: str) -> str:
    return read_csv_summary(filename=filename)

@mcp.tool()
def headers(filename: str) -> str:
    return get_csv_headers(filename=filename)

@mcp.tool()
def columnwise_contents(filename: str) -> str:
    return get_columnwise_content(filename=filename)

@mcp.tool()
def rowwise_contents(filename: str) -> str:
    return get_rowwise_content(filename=filename)

@mcp.tool()
def get_csv_synopsis(filename: str) -> str:
    return get_synopsis_of_csv_content(filename=filename)