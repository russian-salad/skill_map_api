from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from database import Base


association_table_specialization_to_skills = Table('association_table_specialization_to_skills', Base.metadata,
    Column('specialization_id', Integer, ForeignKey('specialization.id')),
    Column('skill_id', Integer, ForeignKey('skill.id'))
)

class Specialization(Base):
    '''
    Database model Specialization
    '''
    __tablename__ = "specialization"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    skill = relationship("Skill", secondary=association_table_specialization_to_skills)