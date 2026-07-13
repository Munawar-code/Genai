from langchain_anthropic import AnthropicLLM
from dotenv import load_dotenv

load_dotenv()

llm = AnthropicLLM(model='claude-sonnet-3-5')

response = llm.invoke("What is the capital of pakistan?")

print(response.content)