from pydantic import BaseModel, Field

class OmikuziText(BaseModel):
    運勢: str = Field(..., max_length=2)
    願望: str = Field(..., max_length=40)
    健康: str = Field(..., max_length=40)
    金運: str = Field(..., max_length=40)
    学問: str = Field(..., max_length=40)
    恋愛: str = Field(..., max_length=40)
    神託: str = Field(..., max_length=120)