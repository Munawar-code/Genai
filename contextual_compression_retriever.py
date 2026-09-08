""" The contextual compression retriever is a an advanced retriever that improves retrieval quality by compressing docs after retrieval by keeping the relevant content based on the user's query.
Query: "What is Photosynthesis?"

Retrieved Doc by traditional retriever: "Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy that can later be released to fuel the organisms' activities. This chemical energy is stored in carbohydrate molecules, such as sugars, which are synthesized from carbon dioxide and water – hence the name photosynthesis, from the Greek phōs (φῶς), 'light', and sunthesis (σύνθεσις), 'putting together'. In most cases, oxygen is also released as a waste product. Most plants, most algae, and cyanobacteria perform photosynthesis; such organisms are called photoautotrophs."

Problem: The retriever returns entire para, only one sentence is actually relevant to the query and the rest is irrelevant noise that wastes context window and may confuse the LLM.

This retriever returns only the relevant part.

How it works: there is a bases retriever e.g. FAISS, Chroma retreives N docs. A compressor usually an LLM is applied to each doc. The compressor keeps only the parts relevant to the query. Irrelevant content is discarded.

When to use: your docs are long and contain mix information, you want to reduce context length for llms, and you need to improve answer accuracy in RAG pipelines.
"""
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_retrievers.contextual_compression import ContextualCompressionRetriever
from langchain_core.documents import Document

docs = [
Document(page_content=('Photosynthesis is a process used by plants and other organisms to convert light energy into chemical energy that can later be released to fuel the organisms\' activities. This chemical energy is stored in carbohydrate molecules, such as sugars, which are synthesized from carbon dioxide and water – hence the name photosynthesis, from the Greek phōs (φῶς), "light", and sunthesis (σύνθεσις), "putting together". In most cases, oxygen is also released as a waste product. Most plants, most algae, and cyanobacteria perform photosynthesis; such organisms are called photoautotrophs.'), metadata={"source": "Wikipedia"}),
Document(page_content=("Langchain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more."), metadata={"source": "Wikipedia"})
]

embedding_model = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(docs, embedding_model)

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(base_compressor=compressor, base_retriever=vectorstore.as_retriever(search_kwargs={"k": 2}))

query = "What is Photosynthesis?"

compressed_results = compression_retriever.invoke(query)