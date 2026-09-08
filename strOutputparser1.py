from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

template = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = template | model | parser | template2 | model | parser

result = chain.invoke({"topic": "black hole"})

print(result)

# The main benefit of string output parser is that it is being used with chains as it is in this particular scenario because parse takes the string output from the model and pass it to template2 without parse we had to make two separate flows like in the case of strOutputparser.py file. 
