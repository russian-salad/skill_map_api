from sqlalchemy import Column, Integer, String

from . import Base

class Specialization(Base):
    '''
    Database model Spezialization
    '''
    __tablename__ = "Specialization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)