from fastapi.encoders import jsonable_encoder
#from app.routers.specializations import update_specialization
from .models.specializations import Specialization
from sqlalchemy.orm import Session

from database.models import specializations
from schemas.specializations import SpecializationBase, SpecializationUpdate
from database.models import skills
from schemas.skills import SkillBase

'''
    запросы для specializations
'''

def get_all_specializations(session: Session):
    return session.query(specializations.Specialization).filter().all()

def get_one_specialization(session: Session, id: int):
    return session.query(specializations.Specialization).filter(specializations.Specialization.id == id).first()

def get_specialization_by_name(session: Session, name: str):
    return session.query(specializations.Specialization).filter(specializations.Specialization.name == name).first()   

def create_specialization(session: Session, specialization: SpecializationBase ):
    new_specialization = specializations.Specialization(name=specialization.name,  description=specialization.description)

    session.add(new_specialization)
    session.commit()
    session.refresh(new_specialization)
    return new_specialization

def delete_specialization(session: Session, name: str):
    current_specialization = session.query(specializations.Specialization).filter(specializations.Specialization.name == name).first() 
    session.delete(current_specialization)
    session.commit()
    return current_specialization

def  make_changes(session: Session, id: int, specialization: SpecializationBase):
    stored_specialization = session.query(specializations.Specialization).filter(specializations.Specialization.id == id).first()
    stored_specialization_model = Specialization(**stored_specialization)
    update_data = specialization.dict(exclude_unset=True)
    update_current_specialization = stored_specialization_model.copy(update=update_data)
    specializations[id] = jsonable_encoder(update_current_specialization)
    return update_current_specialization

'''
    запросы для skills
'''

def get_all_skills(session: Session):
    return session.query(skills.Skill).filter().all()