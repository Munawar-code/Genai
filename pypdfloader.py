from langchain_community.document_loaders import PyPDFLoader
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


loader = PyPDFLoader("sample.pdf")

docs = loader.load()

print(len(docs)) # This will print the number of documents in the list.

print(docs[0].page_content) # This will print the content of the first document in the list.
print(docs[0].metadata) # This will print the metadata of the first document in the list.


""" This pypdf loader has its limitations since it is not good with scanned documents but there are other pdf loaders with specific usecases which can be used and they are the following: PyPDFLoader for Simple, clean PDFs, PDFPlumberLoader for PDFs with tables/columns, UnstructuredPDFLoader or AmazonTextractPDFLoader for scanned or image PDFs, PyMuPDFLoader for need layout and image data, UnstructuredPDFLoader for best structure extraction.""" 