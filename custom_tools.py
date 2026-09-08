"""Tool making is a three step process:
Let's assume our LLM can not perform multiplication. We want to create a tool that can multiply two numbers. The three steps are:
1. Create a function that performs the multiplication. But it is higly recommended to add a docstring to the function which tells the LLM what this function does.
2. Add type hinting in the second step. This tells the LLM what type of input the function expects and what type of output it returns.
3. You apply the @tool decorator to the function. This tells the LLM that this function is a tool and can be used to perform a specific task.
You can call this function's name as your tool. Since this tool is a runnable so you can call it by using the invoke method. The invoke method takes a string as input and returns a string as output. The input string is passed to the function as an argument and the output string is returned by the function.
--> There are three ways to create custom tools in LangChain. Which are the following:
    1. Using @tool decorator
    2. Using StructuredTool & Pydantic: a special type of tool where the input to the tool follows a structured schema, typically defined using a Pydantic model. It is more strict way of creating tools.
    3. Using BaseTool class: is the abstract base class for all the tools in LangChain. It defines the core structure and the interface that any tool must follow, whether it's a simple one-liner or a fully customized function. All other types like @tool and StructuredTool are built on top of BaseTool. This way gives you more deep level implementation and you can also create an async version of your tool also.
""" 


from langchain_core.tools import tool, StructuredTool, BaseTool
from pydantic import BaseModel, Field
from typing import Type

# The below way of creating a tool is done via @tool decorator.

# 1:


def multiply(a, b):
    """This function takes two numbers as input and returns their product."""
    return a * b

# 2:
def multiply(a: int, b: int) -> int:
    """This function takes two integers as input and returns their product as an integer."""
    return a * b 

# 3: 
@tool
def multiply(a: int, b: int) -> int:
    """This function takes two integers as input and returns their product as an integer."""
    return a * b

result = multiply.invoke({"a": 5, "b": 10})

print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)

"""Whenever you send this tool to the LLM, it not see this tool rather it sees the name, description and args of the tool. The LLM can use this information to understand what this tool does and how to use it. The LLM can then call this tool by using the invoke method and passing the required arguments as a dictionary. The invoke method will return the output of the function as a string."""

print(multiply.args_schema.model_json_schema())

"""LLM will never see the logic of that tool rather it sees  this schema: {'description': 'This function takes two integers as input and returns their product as an integer.', 'properties': {'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}, 'required': ['a', 'b'], 'title': 'multiply', 'type': 'object'}"""

# This below way of creating custom tools is via StructuredTool approach:

# 1. Like before you will make a function first:
class MultiplyInput(BaseModel):
    x: int = Field(required=True, description="The first number to add")
    y: int = Field(required=True, description="The second number to add")

# Here is the function and if you want you can not use the type hinting because you have made a pydantic class before as above and here we have given the attributes with their types, and extra description also added for these two fields.

def multiply_func(x, y):
    return x * y

multiply_tool = StructuredTool.from_function(
    func=multiply_func,
    name="multiply",
    description="Product of two numbers",
    args_schema=MultiplyInput
)

result = multiply_tool.invoke({"x":6, "y":5})

print(result)
print(multiply_tool.name)
print(multiply_tool.description)

print(multiply_tool.args_schema.model_json_schema())

"""This is the schema that will be seen by the LLM in case of StructureTool approach: {'properties': {'x': {'description': 'The first number to add', 'required': True, 'title': 'X', 'type': 'integer'}, 'y': {'description': 'The second number to add', 'required': True, 'title': 'Y', 'type': 'integer'}}, 'required': ['x', 'y'], 'title': 'MultiplyInput', 'type': 'object'}"""


# This below way of creating custom tools is done via using BaseTool abstract class:

# 1. Firstly you have to make your own class which will inherit base tool class:
class MultiplyTool(BaseTool):
    name: str = "product"
    description: str = "Product of two digits"

    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, x: int, y: int) -> int:
        return x * y

multiply_num = MultiplyTool()

results = multiply_num.invoke({'x': 10, 'y': 25})

print(results)
print(multiply_num.name)
print(multiply_num.description)

print(multiply_num.args)

print(multiply_num.args_schema.model_json_schema())

"""This is what the LLM sees in case of Basetool approach: {'x': {'description': 'The first number to add', 'title': 'X', 'type': 'integer'}, 'y': {'description': 'The second number to add', 'title': 'Y', 'type': 'integer'}}
{'properties': {'x': {'description': 'The first number to add', 'required': True, 'title': 'X', 'type': 'integer'}, 'y': {'description': 'The second number to add', 'required': True, 'title': 'Y', 'type': 'integer'}}, 'required': ['x', 'y'], 'title': 'MultiplyInput', 'type': 'object'}"""