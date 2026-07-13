from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Pakistan is a south asian country.",
    "Uzbekistan is a central asian country.",
    "India is a south asian country."
]

result = embedding.embed_documents(documents)      # this embed_documents function has the capability of generating the embeddings of multiple docs in a single run or collectively.

print(str(result))
