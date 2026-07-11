from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

text = 'Delhi is the capital of India'

vector = embedding.embed_query(text) # we can also use the embed_documents function to pass multiple docs or sentences and generate their embeddings simultaneously.

print(str(vector))