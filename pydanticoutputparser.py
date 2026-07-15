from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="age of the person")
    city: str = Field(description="Name of the city of the belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age, and city of a {place} person \n {format_instructions}",
    input_variables = ['place'],
    partial_variables = {"format_instructions":parser.get_format_instructions()}
)

chain = template | model | parser

final_result = chain.invoke({"place": "American"})

print(final_result)