from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(path="books", glob="*.pdf", loader_cls=PyPDFLoader)

docs = loader.load()

print(len(docs)) # This will print the number of documents in the list.

print(docs[0].page_content) # This will print the content of the first document in the list.
print(docs[0].metadata) # This will print the metadata of the first document in the list.

""" This directory loader takes time while loading all the pdfs from a specific given directory and as the number of files increases the time taken to load all the files also increases. So to overcome this problem there is a concept of lazy loading in LangChain which is used to load the files on demand or one by one because it gives a generator of documents instead of a list of documents. So we can use the lazy loading concept to load the files one by one instead of loading all the files at once which is done by load function which does eager loading means all the documents at once. Lazy load is best when dealing with large documents  or lots of documents or files. It is also better when stream processing like chunking, embedding without using lots of memory. When the number of docs is smaller or the docs are smaller in size or you want to load everything upfront then load function is better."""