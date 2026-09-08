from langchain.text_splitter import RecursiveCharacterTextSplitter,Language


text = """ class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b 
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=language.PYTHON,
    chunk_size=100,
    chunk_overlap=0,
    separators=''
) # chunk_overlap tells us how much overlap we want between two characters. It is useful in terms of retaining the context of the text. For example, if we have a chunk size of 100 and an overlap of 20, then the first chunk will be from 0 to 100, and the second chunk will be from 80 to 180. This way, we can retain the context of the text. But there is a trade-off between chunk size and overlap. If we have a large chunk size and a small overlap, then we will lose the context of the text. On the other hand, if we have a small chunk size and a large overlap, then we will retain the context of the text but at the cost of having more chunks. So, we need to find a balance between chunk size and overlap.

chunks = splitter.split_text(text) # In case of documents we will use the split_documents method instead of split_text method.

print(chunks)

print(len(chunks)) # This will print the number of chunks generated from the text.
prints(chunks[0])
