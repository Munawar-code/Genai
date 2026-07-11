from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model='claude-sonnet-4-6')

response = llm.invoke("What is the capital of pakistan?")

print(response.content)