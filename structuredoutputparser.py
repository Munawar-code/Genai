from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")


schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic."),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic."),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic.")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = model.invoke(prompt)

print(result)

You can only tell the structure in which you want the output but you can not do or perform data validation in case of structureoutput parsers.