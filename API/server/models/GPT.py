from typing import Optional

from pydantic import BaseModel, Field


class GPTSchema(BaseModel):
    """GPT Q&A Model"""

    db_schema: list = Field(..., description="Database Schema")
    question: str = Field(..., title="Question", description="Question from User")
    settings: dict = Field(
        ..., title="Settings", description="Settings for the Question"
    )

    class Config:
        schema_extra = {
            "example": {
                "db_schema": [
                    "id_field : text_FIELD",
                    "name_field : text_TYPE",
                    "score_field : text_TYPE",
                ],
                "question": "which name having score more than 6",
                "settings": {"model_ver": "baseline"},
            }
        }
