from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from database import query
from database import SessionLocal
from schemas.skills import SkillBase
from dependencies.db import get_db

router = APIRouter()

@router.get('/all_skills', response_model=List[SkillBase])
async def get_all_skills(session: Session = Depends(get_db)):
    return query.get_all_skills(session)