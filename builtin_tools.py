from langchain_community.tools import DuckDuckGoSearchRun, ShellTool
""""
search_tool = DuckDuckGoSearchRun()
results = search_tool.invoke("What is the current breaking news in silicon valley today?")

print(results) """

shell_tool = ShellTool()
results = shell_tool.invoke("ls -l")
print(results)



