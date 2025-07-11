from fastapi import FastAPI
from flasx.database import engine
from flasx.models.user_model import Base as UserBase

from flasx.routers import (
    register_router,
    auth_router,
)

UserBase.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(register_router.router)
app.include_router(auth_router.router)
