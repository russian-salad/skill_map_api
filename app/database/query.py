from sqlalchemy.orm import Session

from database.models import specializations


def get_all_specializations(session: Session):
    
    return session.query(specializations.Specialization).filter().all()