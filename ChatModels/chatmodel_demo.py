from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

response = model.invoke("write a function in python for fibonnaci sequence")

print(response)