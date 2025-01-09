from typing import List, Dict, Any
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from pydantic import BaseModel, Field


class Summary(BaseModel):
    summary: str = Field(description="Summary")
    facts: List[str] = Field(description="interesting facts about them")
    korean_answer: str = Field(description="Answer in Korean language")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "facts": self.facts,
            "korean_answer": self.korean_answer
        }
    

summary_parser = PydanticOutputParser(pydantic_object=Summary)