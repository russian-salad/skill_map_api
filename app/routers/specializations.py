from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List


from database import query
from database import SessionLocal
from schemas.specializations import SpecializationBase
from dependencies.db import get_db

router = APIRouter()


@router.get('/all_specializations', response_model=List[SpecializationBase])
async def get_all_specializations(session: Session = Depends(get_db)):
    return query.get_all_specializations(session)


@router.get('/all_specialization/{id}', response_model=SpecializationBase)
async def get_one_specialization(id: int,session: Session = Depends(get_db)):
    return query.get_one_specialization(session, id)


@router.post('/add_specialization', response_model=SpecializationBase)
async def create_specialization(specialization: SpecializationBase, session: Session = Depends(get_db)):
    current_specialization = query.get_specialization_by_name(session, name=specialization.name)
    if current_specialization:
        raise HTTPException(status_code=400, detail="Specialization already exists")
    return query.create_specialization(session, specialization)


@router.delete('/delete_specialization', response_model=SpecializationBase)
async def delete_specialization(specialization: SpecializationBase, session: Session = Depends(get_db)):
    print(specialization.name)
    current_specialization = query.get_specialization_by_name(session, name=specialization.name)
    if current_specialization:
        return query.delete_specialization(session, name = specialization.name)
    else: 
        raise HTTPException(status_code=400, detail="Specialization does not exist")
    
