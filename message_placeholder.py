from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template creation

# A message placeholder is a special placeholder used inside chat prompt template to dynamically insert chat history or a list of messages at runtime. It allows for the inclusion of previous messages in the conversation, enabling the model to maintain context and continuity in its responses. The MessagesPlaceholder class is used to define this placeholder within the chat prompt template, specifying the variable name that will hold the chat history or messages to be inserted when invoking the prompt.
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name="chat_history"), 
    ('human', "{query}")
])

chat_history = [] 
# load chat history from a file or database
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

# create prompt
prompt = chat_template.invoke({"chat_history": chat_history, "query":"Where is my refund?"})

print(prompt)