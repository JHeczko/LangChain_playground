from typing import Dict, List, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="Summary text")
    facts: List[str] = Field(description="Facts list")

    def to_dict(self) -> Dict[str, Any]:
        return {"summary": self.summary, "facts": self.facts}

summary_parser = PydanticOutputParser(pydantic_object=Summary)

if __name__ == "__main__":
    print(summary_parser.get_format_instructions())