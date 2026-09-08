RAG is a technique that combines information with language generation, where a model retrieves relevant documents from a knowledge base and then uses them as context to generate accurate and grounded responses. 
Benefits of using RAG is use of up to date information, better privacy and no limit document size.

 Components of RAG in LangChain: 
    1. Document Loaders
    2. Text Splitters
    3. Vector Databases
    4. Retrievers

1. Document Loaders are components in LangChain used to load data from various sources into a standardized format usually as document objects which can then be used for chunking, embedding, retrieval and generation.


This document is the standardized format in the langchain:
   Document(
       page_content="The actual text content",
      metadata={"source":"filename.pdf", .....})

-> Types of Document Loaders:
   1. TextLoader is a simple and commonly used document loader in LangChain that reads plain text (.txt) files and converts them into LangChain Document objects. It is ideally used for loading chat logs, scraped text, transcripts, code snippets, or any plain text data into a LangChain pipeline.
   Limitation: It only works with .txt files. 

   2. PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert each page into a document object. This loader works on page by page basis. Let's say we give it a pdf file of 25 pages it will give use 25 document objects from that single file.
   Limitations: It uses the PyPDF library under the hood and not great with scanned PDFs or complex layouts.

   3. DirectoryLoader is a document loader that lets you load multiple documents from a directory folder of files.

   4. WebBaseLoader is a document loader that is used to load and extract text content from web pages (URLs). It uses BeautifulSoup under the hood to parse HTML and extract visible text. It should be used when dealing with blogs, news articles, or public websites where the content is primarily text-based and static.
   Limitations: Doesn't handle javascript heavy pages well (use SeleniumURLLoader for that). Loads only static content what's in the HTML not what loads after the page renders.

   5. CSVLoader is a document loader used to load CSV files into LangChain document objects one per row by default.

2. Text Splitters are components of LangChain used to split or break large chunks of text like articles, pdfs, html pages or books into smaller manageable pieces(chunks) that an LLM can handle effectively.
Why text splitting is important in making LLM powered apps? 
   1. It overcomes model limitations because many embedding models and language models have max input size constraints i.e. context length limit. Splitting allows us to process docs that would otherwise exceed these limits.
   2. Text splitting improves nearly every LLM powered task like embedding, semantic search, and summarization. 
   3. It helps in optimizing computational resources since working with smaller chunks of text can be more efficient and allow for better parallellization of processing tasks.
Text splitters are of four types in Langchain namely Length based, Text Structure Based, Document Structure Based and Semantic Meaning Based. 
   1. Length Based Text Splitting here you initially decide about the length of the chunks or the size of the chunks which can be either in characters or in tokens. Lets say the chunk size is 100 characters so in a given paragraph you will start from the first character and stop at 100th character this will be Chunk 1 and then Chunk 2 will be from 101st character till 200th character and so on but this splitting is irrespective of grammar, sentence structure or context and even spelling completion. So in case of embedding generation your embeddings won't capture the complete semantic meanings.
   2. Text-Structured Based it considers that any kind of text follows an inherent text structure means first you organise your text in paragraphs and then you organize in sentences and then you organize words in those sentences this hierarchy of structuring is being utilized by this particular technique.
   3. Document-Structured Based: let's say you are working with a document which is in a totally different format like you have a piece of code and you have to process it using an LLM it is also text but not normal text which you split in paras or lines or characters because it is organized in a totally different way like a class define in programming which has different methods. We also use the recursive character text splitter but in a different way because here the separators are different like "\nclass", "n\def", "\n\tdef" after using these then we use the normal separators "\n\n", "\n", " ", "" for paragraph, line, space based separation. This can also be used for md files text also and it has its own separators. 
   4. Semantic Meaning Based is used when you have to make chunks on the basis of semantic not on the basis of text structure or document structure. Let's say we have two paras in the first para the first sentence is about weather and crops and the second sentence about champions league football, and the second para is about terrorism so here we split these three and then give them to an embedding model to get embeddings of first sentence, 2nd and the 2nd para and compare these with each other to find their cosine similarity at any given point where you find that the score for the cosine similarity between two given sentences or paras is low this means the topic of both paras is different so it will be the point to make chunk.
3. Vector Stores
4. Retrievers in langchain are used to fetch relevant docs from a data source in response to a user query. There are multiple types of retrievers in langchain and all these retrievers are runnables. Retriever is just like a function and it takes a user query and go to the data source which can be a vector store or an api and search the data source to extract relevant documents and provide multiple document objects in the output. You can also use retrievers for making chains or you can plug in retrievers in the existing chains. 
   1. Retrievers on the basis of data sources: Each retriever works with a specific data source like wikipedia retriever, vector store retriever and arxiv retriever.
   2. Retrievers on the basis of search strategy: Some categories of retrievers are on the basis of their search mechanism like MMR, multi-query retriever, and contextual compression retriever.

