from pydantic import BaseModel, Field
from typing import Any

class BlogPostCreate(BaseModel):
    title: str = Field(..., example="My First Blog")
    slug: str = Field(..., example="my-first-blog")
    category: str = Field(..., example="my-first-blog")
    content_json: dict[str, Any] = Field(..., example={
        "type": "doc",
        "content": [
            {
                "type": "paragraph",
                "attrs": {"textAlign": None},
                "content": [
                    {"type": "text", "text": "Write your amazing story here..."}
                ]
            }
        ]
    })


class CategoryCreate(BaseModel):
    name: str
