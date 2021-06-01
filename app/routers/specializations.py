from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List


from database import query
from database import SessionLocal
from schemas.specializations import SpecializationBase
from dependencies.db import get_db

router = APIRouter()


@router.get('/all_spezialisation', response_model=List[SpecializationBase])
async def get_all_spezialisation(session: Session = Depends(get_db)):

    return query.get_all_specializations(session)


