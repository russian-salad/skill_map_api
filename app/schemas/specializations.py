from typing import List, Optional
from pydantic import BaseModel

class SpecializationBase(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class SpecializationUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True