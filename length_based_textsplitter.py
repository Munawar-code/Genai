from langchain.text_splitter import TextSplitter

text = """ The government takes the billions of rupees collected from public prize bond sales and deposits them into the State Bank of Pakistan (SBP). Instead of letting this cash sit idle, the government uses it to:Fund national infrastructure, public utilities, and development projects.Reduce its reliance on expensive foreign debt or high-interest bank borrowing.Generate economic returns through state revenue channels"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separators=''
) # chunk_overlap tells us how much overlap we want between two characters. It is useful in terms of retaining the context of the text. For example, if we have a chunk size of 100 and an overlap of 20, then the first chunk will be from 0 to 100, and the second chunk will be from 80 to 180. This way, we can retain the context of the text. But there is a trade-off between chunk size and overlap. If we have a large chunk size and a small overlap, then we will lose the context of the text. On the other hand, if we have a small chunk size and a large overlap, then we will retain the context of the text but at the cost of having more chunks. So, we need to find a balance between chunk size and overlap.

result = splitter.split_text(text) # In case of documents we will use the split_documents method instead of split_text method.

print(result)

