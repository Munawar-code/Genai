"""How can we pick results that are not only relevant but also different from each other?
MMR is an information retrieval algorithm designed to reduce redundancy in the retrieved results while maintaining high relevance to the query. 
Why MMR Retriever?
In regular similarity search, you may get docs that are:
  1. All very similar to each other.
  2. Repeating same information.
  3. Lacking diverse perspectives.

MMR Retriever avoids that by: picking the most relevant doc first, then picking then next most relevant and least similar to already selected docs and so on. This helps in rag pipelines where you want your context window to contain diverse but still relevant information, especially useful when docs are semantically overlapping.
""" 

docs = [
    Document(page_content="The government takes the billions of rupees collected from public prize bond sales and deposits them into the State Bank of Pakistan (SBP). Instead of letting this cash sit idle, the government uses it to:Fund national infrastructure, public utilities, and development projects.Reduce its reliance on expensive foreign debt or high-interest bank borrowing.Generate economic returns through state revenue channels"),
    Document(page_content="Langchain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more.")]

from langchain_community.vectorstores import FAISS

embedding_model = AnthropicEmbeddings()

vectorstore = FAISS.from_documents(documents=docs, embedding=embedding_model)

# enable MMR retriever
retriever = vectorstore.as_retriever(search_type="mmr", search_kwargs={"k": 2, "lambda_mult": 0.5})

query = "What is langchain?"
results = retriever.invoke(query)

