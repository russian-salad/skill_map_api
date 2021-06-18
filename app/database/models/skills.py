from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from database import Base
from . import sources

association_table_skill_to_source = Table('association_table_skill_to_source', Base.metadata,
    Column('skill_id', Integer, ForeignKey('skill.id')),
    Column('source_id', Integer, ForeignKey('source.id'))
)
class Skill(Base):
    '''
    Database model Skill
    '''
    __tablename__ = "skill"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    source = relationship('Source', secondary=association_table_skill_to_source)