from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Skills(Base):
    '''
    Database model Skills
    '''
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    source = relationship("Sources")