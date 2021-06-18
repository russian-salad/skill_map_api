from typing import List, Optional
from pydantic import BaseModel

class SkillBase(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

