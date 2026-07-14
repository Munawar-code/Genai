

from langchain_anthropic import ChatAnthropic
from typing import TypedDict, Optional, Annotated
from dotenv import load_dotenv
from pydantic import BaseModel, Field


load_dotenv()

model = ChatAnthropic(model="claude-opus-4-8")

# Defining a Schema
# This below was a simple typeddict. This can be risky because the model generated the summary not in a desired way.
"""class Review(TypedDict):
    summary: str
    sentiment: str
"""
# Here we are using pydantic
class Review(BaseModel):
    key_themes: list[str] = Field(description="The key themes of the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="The sentiment of the review, either positive, negative, or neutral")
    pros: Optional[list[str]] = Field(default=None, description= "Write down all the pros in a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons in a list")
    name: Optional[str] = Field(default=None, description="Write the name of the reviewer")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""The hardware is great but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result.name)



