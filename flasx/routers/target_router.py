from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from flasx.database import get_db
from flasx.models.target_model import TargetProvince
from flasx.models.user_model import User
from flasx.models.province_model import Province
from flasx.schemas.target_schema import TargetProvinceOut, TargetProvinceCreate
from flasx.core.config import settings
from jose import jwt, JWTError
from typing import List

# Define the OAuth2 scheme 
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Create a new API router with prefix /targets
router = APIRouter(prefix="/targets", tags=["targets"])

# Dependency to get the current user from JWT token
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"]) # Decode the JWT token 
        username = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = db.query(User).filter(User.username == username).first() # Fetch the user from the database using the decoded username
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

# Endpoint to add a target province for the current user
@router.post("/", response_model=TargetProvinceOut)
def add_target(
    target: TargetProvinceCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    # Check if the province exists
    province = db.query(Province).filter(Province.id == target.province_id).first()
    if not province:
        raise HTTPException(status_code=404, detail="Province not found")
    
    # Create and save the new target province for the user
    new_target = TargetProvince(user_id=user.id, province_id=province.id)
    db.add(new_target)
    db.commit()
    db.refresh(new_target)
    
    return new_target

# Endpoint to list all target provinces selected by the current user
@router.get("/", response_model=List[TargetProvinceOut])
def list_targets(db: Session = Depends(get_db), user=Depends(get_current_user)):
    targets = db.query(TargetProvince).filter(TargetProvince.user_id == user.id).all()
    return targets
