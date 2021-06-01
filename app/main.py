from fastapi import FastAPI

from routers import specializations
from database import Base
from database.engine import engine


Base.metadata.create_all(bind=engine)

app = FastAPI()



app.include_router(specializations.router)