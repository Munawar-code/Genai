RAG is a technique that combines information with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses. 
Benefits of using RAG is use of up to date information, better privacy and no limit document size.

 Components of RAG: 
    1. Document Loaders
    2. Text Splitters
    3. Vector Databases
    4. Retrievers

1. Document Loaders are components in LangChain used to load data from various sources into a standardized format usually as document objects which can then be used for chunking, embedding, retrieval and generation.

Document(
   page_content="The actual text content",
   metadata={"source":"filename.pdf", .....}
)
-> Types of Document Loaders:
   1. TextLoader is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects. It is ideally used for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.
   It only works with .txt files. 

   2. 