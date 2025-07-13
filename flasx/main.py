from fastapi import FastAPI
from flasx.database import engine
from flasx.models.user_model import Base as UserBase
from flasx.models.province_model import Base as ProvinceBase
from flasx.models.target_model import Base as TargetBase

from flasx.routers import (
    register_router,
    auth_router,
    province_router,
    target_router
)

UserBase.metadata.create_all(bind=engine)
ProvinceBase.metadata.create_all(bind=engine)
TargetBase.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to the backend of the Thai Travel project"}

app.include_router(register_router.router)
app.include_router(auth_router.router)
app.include_router(province_router.router)
app.include_router(target_router.router)
