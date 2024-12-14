from pydantic import BaseModel, Field

class Requestgpt(BaseModel):
    text : str = Field(...)
    thread_id : str = Field(...)
      