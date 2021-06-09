from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from database import Base

class Sources(Base):
    '''
    Database model Sources
    '''
    __tablename__ = "Source"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    skill_id = Column(Integer, ForeignKey('skill.id'))