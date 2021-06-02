from sqlalchemy.orm import Session

from database.models import specializations
from schemas.specializations import SpecializationBase

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