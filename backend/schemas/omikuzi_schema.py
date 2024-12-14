from pydantic import BaseModel, Field

class OmikuziText(BaseModel):
    運勢: str = Field(...)
    願望: str = Field(...)
    健康: str = Field(...)
    金運: str = Field(...)
    学問: str = Field(...)
    恋愛: str = Field(...)
    神託: str = Field(...)