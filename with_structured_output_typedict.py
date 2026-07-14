# TypedDict is only useful for representation of the output. It does not enforce any validation on the output. The model can still generate output that does not conform to the TypedDict schema. Therefore, using Pydantic model is a better approach for enforcing validation on the output.

from langchain_anthropic import ChatAnthropic
from typing import TypedDict, Optional, Annotated
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

# Defining a Schema
# This below was a simple typeddict. This can be risky because the model generated the summary not in a desired way.
"""class Review(TypedDict):
    summary: str
    sentiment: str
"""
# here we are using annotated tyeddict to provide more context to the model about the expected output. This helps the model to generate a more accurate and structured response.
class Review(TypedDict):
    key_themes: Annotated[str, "The key themes of the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review, either positive, negative, or neutral"] # We can also use literal types to restrict the sentiment to only positive, negative, or neutral. But for this example, we will keep it simple and use str.
    pros: Annotated[Optional[list[str]], "Write down all the pros in a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons in a list"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)
print(result["summary"])
print(result["sentiment"])


