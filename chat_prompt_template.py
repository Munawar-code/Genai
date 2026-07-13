from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

"""chat_template = ChatPromptTemplate([
    SystemMessage(content="You are a helpful {domain} expert"), #By using these two classes when we run this file we will get a prompt that has a list of messages with these placeholders which is not filled yet. Therefore we will use another way and that is to use a tuple having the role and the string in the parameters of the ChatPromptTemplate class. The role can be system, human or AI. The string can have placeholders which will be filled later when we invoke the prompt template. This way we can create a structured chat history with the role and the message content.
    HumanMessage(content="Explain in simple terms, what is {topic}")
])"""

chat_template = ChatPromptTemplate([
        ("system", "You are a helpful {domain} expert"),
        ("human", "Explain in simple terms, what is {topic}")]
)

prompt = chat_template.invoke({"domain": "AI", "topic": "Model Context Protocol"})

print(prompt)