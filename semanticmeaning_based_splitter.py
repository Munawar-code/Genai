from langchain_experimental.text_splitter import SemanticChunker
from langchain_anthropic.embeddings import AnthropicEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker((AnthropicEmbeddings(), breakpoint_threshold="standard_deviation"), breakpoint_threshold_amount=1))


Sample = """ The government takes the billions of rupees collected from public prize bond sales and deposits them into the State Bank of Pakistan (SBP). Instead of letting this cash sit idle, the government uses it to:Fund national infrastructure, public utilities, and development projects.Reduce its reliance on expensive foreign debt or high-interest bank borrowing.Generate economic returns through state revenue channels"""

docs = text_splitter.split_text([Sample])

