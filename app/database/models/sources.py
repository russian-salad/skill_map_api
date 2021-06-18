from sqlalchemy import Column, Integer, String


from database import Base

class Source(Base):
    '''
    Database model Source
    '''
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)