

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
# Here we are using json schema
json_schema = {
  "$schema": "http://json-schema.org",
  "title": "ProductReview",
  "type": "object",
  "properties": {
    "reviewId": {
      "type": "string",
      "description": "Unique identifier for the review.",
      "format": "uuid"
    },
    "productId": {
      "type": "string",
      "description": "Unique identifier for the product being reviewed."
    },
    "productName": {
      "type": "string",
      "description": "Name of the product."
    },
    "author": {
      "type": "object",
      "description": "Information about the reviewer.",
      "properties": {
        "userId": {
          "type": "string",
          "description": "Unique identifier for the user."
        },
        "username": {
          "type": "string",
          "description": "Public display name of the reviewer."
        },
        "isVerifiedPurchaser": {
          "type": "boolean",
          "description": "Indicates if the reviewer bought the product from the platform."
        },
        "badge": {
          "type": "string",
          "description": "Role or status of the reviewer (e.g., 'Top Contributor', 'Verified Expert')."
        }
      },
      "required": ["userId", "username", "isVerifiedPurchaser"]
    },
    "rating": {
      "type": "object",
      "properties": {
        "score": {
          "type": "number",
          "minimum": 1.0,
          "maximum": 5.0,
          "description": "The numerical rating given to the product."
        },
        "title": {
          "type": "string",
          "description": "A short, catchy summary or headline for the review."
        },
        "pros": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of positive highlights about the product."
        },
        "cons": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of negative aspects or drawbacks of the product."
        }
      },
      "required": ["score", "title"]
    },
    "body": {
      "type": "string",
      "description": "The detailed text content of the review."
    },
    "dateCreated": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp when the review was initially submitted."
    },
    "dateUpdated": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp when the review was last modified."
    },
    "media": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "mediaId": {
            "type": "string"
          },
          "url": {
            "type": "string",
            "format": "uri"
          },
          "type": {
            "type": "string",
            "enum": ["image", "video"]
          },
          "caption": {
            "type": "string"
          }
        },
        "required": ["mediaId", "url", "type"]
      },
      "description": "Photos or videos attached to the review."
    },
    "metrics": {
      "type": "object",
      "properties": {
        "helpfulVotes": {
          "type": "integer",
          "minimum": 0,
          "description": "Number of users who marked this review as helpful."
        },
        "totalVotes": {
          "type": "integer",
          "minimum": 0,
          "description": "Total number of users who voted on this review."
        },
        "recommended": {
          "type": "boolean",
          "description": "Whether the reviewer explicitly recommends the product to others."
        }
      },
      "required": ["helpfulVotes", "totalVotes"]
    },
    "productAttributes": {
      "type": "object",
      "properties": {
        "size": {
          "type": "string",
          "description": "Specific size of the product, if applicable (e.g., clothing)."
        },
        "color": {
          "type": "string",
          "description": "Color variant of the product."
        },
        "condition": {
          "type": "string",
          "enum": ["New", "Like New", "Good", "Fair", "Poor"]
        }
      }
    }
  },
  "required": [
    "reviewId",
    "productId",
    "productName",
    "author",
    "rating",
    "body",
    "dateCreated",
    "metrics"
  ]
}

structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""The hardware is great but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)



