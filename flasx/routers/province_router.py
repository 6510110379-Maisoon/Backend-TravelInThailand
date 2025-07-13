from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from flasx.database import get_db
from flasx.models.province_model import Province
from flasx.schemas.province_schema import ProvinceOut, ProvinceBase

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

from flasx.schemas.province_schema import ProvinceOut, ProvinceBase  # <- อย่าลืมนำเข้า ProvinceBase

@router.post("/", response_model=ProvinceOut)
def create_province(province: ProvinceBase, db: Session = Depends(get_db)):
    existing = db.query(Province).filter(Province.name == province.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Province already exists")
    new_province = Province(**province.dict())
    db.add(new_province)
    db.commit()
    db.refresh(new_province)
    return new_province

