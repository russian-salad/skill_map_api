from fastapi import FastAPI

from routers import specializations, skills
from database import Base
from database.engine import engine


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(specializations.router)
app.include_router(skills.router)