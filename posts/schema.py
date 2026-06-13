from pydantic import BaseModel, ConfigDict
from typing import Optional


class AuthorCreateSchema(BaseModel):
    name:str
   

class AuthorUpdateSchema(BaseModel):
    name : Optional[str] = None

