"""A toolkit is just a collection of related tools that serve a common purpose packaged together for convenience and reusability. In Langchain a toolkit might GoogleDriveToolkit and it can contain tools like: GoogleDriveCreateFileTool, GoogleDriveSearchTool, GoogleDriveReadFileTool."""

from langchain_core.tools import tool

# Custom Tools being made which will be part of the toolkit that we wanna make

@tool 
def add(a: int, b: int) -> int:
    """Add two nums"""
    return a + b

@tool 
def multiply(a: int, b: int) -> int:
    """Product of two nums"""
    return a * b

# Making a class for the toolkit that we wanna make
class MathToolkit:
    def get_tools(self):
        return[add, multiply]


toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)


