from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from flasx.database import get_db
from flasx.models.province_model import Province
from flasx.schemas.province_schema import ProvinceOut

router = APIRouter(prefix="/provinces", tags=["provinces"]) # Create an API router 

@router.get("/", response_model=List[ProvinceOut]) # Route to get a list of all provinces
def get_provinces(db: Session = Depends(get_db)):
    return db.query(Province).all()

@router.get("/primary", response_model=List[ProvinceOut])  # Route to get only primary provinces
def get_primary(db: Session = Depends(get_db)):
    return db.query(Province).filter(Province.is_secondary == False).all()

@router.get("/secondary", response_model=List[ProvinceOut]) # Route to get only secondary provinces
def get_secondary(db: Session = Depends(get_db)):
    return db.query(Province).filter(Province.is_secondary == True).all()
