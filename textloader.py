from langchain_community.document_loaders import TextLoader
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

prompt = PromptTemplate(
    template="Write a summary for the following poem - \n{poem}",
    input_variables=['poem']
)
parser = StrOutputParser()

loader = TextLoader("text.txt", encoding="utf-8")

docs = loader.load()

""" This document loader loads text files or a single document as a list of documents. So one file is splitted into multiple documents based on the number of line in the file. We can use print(type(docs)) to check the type of docs which returns a list. In order to find the number of documents in this list we can use print(len(docs)) which returns the number of documents in the list. If we want to extract the items of this list we can use print(docs[0]) to get the first document in the list. Now if we extract or want to get the type of doc 0 we can use print(type(docs[0])) which returns <class'langchain_core.documents.base.Document'>"""

print(docs[0].page_content) # This will print the content of the first document in the list.

print(docs[0].metadata) # This will print the metadata of the first document in the list.)


chain = prompt | model | parser

chain.invoke({"poem": docs[0].page_content}) # This will invoke the chain with the content of the first document in the list as input to the prompt template.