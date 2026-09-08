""" Sometimes a single query might not capture all the ways information is phrased in your docs. E.g. "How can I stay healthy? this query could mean a lot of things: what should I eat, how often should I exercise, how can I manage stress? etc. 
A simple similarity search might miss docs that talk about those things but don't use the word "healthy". 
This retriever takes your origingal query uses an llm to generate multiple semantically different versions of that query, performs retrieval for each sub-query and combines and deduplicates the results.
"""

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI
from langchain_retrievers.multi_query import MultiQueryRetriever

all_docs = [
    Document(page_content="The government takes the billions of rupees collected from public prize bond sales and deposits them into the State Bank of Pakistan (SBP). Instead of letting this cash sit idle, the government uses it to:Fund national infrastructure, public utilities, and development projects.Reduce its reliance on expensive foreign debt or high-interest bank borrowing.Generate economic returns through state revenue channels"),
    Document(page_content="Langchain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.")
]

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(all_docs, embedding_model)
similarity_retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

multiquery_retriever = MultiQueryRetriever.from_llm(retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
)

query = "how to improve chains in langchain?"

multiquery_results = multiquery_retriever.invoke(query)
