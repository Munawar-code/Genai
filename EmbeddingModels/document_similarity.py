from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

document = [
    "Virat Kohli is an indian cricketer known for his aggressive batting and leadership.",
    "Dhone is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin is also known as the God of Cricket and he holds many records.",
    "Rohit sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about virat kohli"

doc_embeddings = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]

print(document[index])
print("Similarity score is:", score)