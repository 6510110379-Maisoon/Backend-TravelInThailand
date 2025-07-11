from pydantic import BaseModel 
from typing import Optional

# Base schema for a province used for data validation and serialization
class ProvinceBase(BaseModel):
    name: str                          
    is_secondary: bool = False        
    tax_reduction: Optional[int] = 0   

# Schema used for output, includes the province ID
class ProvinceOut(ProvinceBase):
    id: int                            

    class Config:
        orm_mode = True # Enables compatibility with ORM objects 
