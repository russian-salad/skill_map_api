from typing import List, Optional
from pydantic import BaseModel

class SpecializationBase(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True