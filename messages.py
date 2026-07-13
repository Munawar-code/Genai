from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

# HumanMessage is the message send by the user to the LLM. AIMessage is the message send by the LLM to the user in return. SystemMessage is a system level message that sets the context for the conversation. It is used to provide instructions to the LLM on how to respond to the user input. The system message is usually sent at the beginning of the conversation and is not visible to the user. It is used to set the context for the conversation and provide instructions to the LLM on how to respond to the user input.
messages = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
    HumanMessage(content="Tell me the difference between langchain and langgraph.")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)



