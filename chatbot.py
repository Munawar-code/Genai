from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

# Initially we did not maintain a chat history, so the model was not able to remember the previous context of the conversation. To maintain a chat history, we can use a list to store the conversation history and pass it to the model for generating responses.

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
    HumanMessage(content="Tell me the difference between langchain and langgraph.")
]

while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)

print(chat_history)

# But there is a problem with this approach which is when we print the chat history, it will print the entire conversation history including the user input and the model response. This can be a problem because the history will not tell which message is from the user and which message is from the model. To solve this problem, we can use the SystemMessage, HumanMessage, and AIMessage classes from langchain_core.messages to create a structured chat history. Refer to messages.py for that implementation. 