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

app.include_router(register_router.router)
app.include_router(auth_router.router)

