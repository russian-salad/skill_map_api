from sqlalchemy.orm import Session

from database.models import specializations


def get_all_specializations(session: Session):
    return session.query(specializations.Specialization).filter().all()

def get_one_specializations(session: Session, id: int):
    return session.query(specializations.Specialization).filter(specializations.Specialization.id == id).first()