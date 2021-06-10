from sqlalchemy import Column, Integer, Table
from sqlalchemy.sql.schema import ForeignKey

from skills import Skill
from sources import Source
from specializations import Specialization
from database import Base


association_table_skill_to_source = Table('association_table_skill_to_source', Base.metadata,
    Column('skill_id', Integer, ForeignKey(Skill.skill.id)),
    Column('source_id', Integer, ForeignKey(Source.source.id))
)


association_table_specialization_to_skills = Table('association_table_specialization_to_skills', Base.metadata,
    Column('specialization_id', Integer, ForeignKey(Specialization.specialization.id)),
    Column('skill_id', Integer, ForeignKey(Skill.skill.id))
)