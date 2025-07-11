from pydantic import BaseModel
from flasx.schemas.province_schema import ProvinceOut

# creating a new target province (input from user)
class TargetProvinceCreate(BaseModel):
    province_id: int  # ID of the province the user wants to target

# returning a target province (output to client)
class TargetProvinceOut(BaseModel):
    id: int  
    province: ProvinceOut  

    class Config:
        orm_mode = True  # Enable compatibility with ORM models 
