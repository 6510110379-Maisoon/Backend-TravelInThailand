from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from flasx.database import get_db
from flasx.models.user_model import User
from flasx.schemas.user_schema import UserCreate, UserOut
from flasx.core.security import get_password_hash

router = APIRouter(prefix="/register", tags=["register"])

@router.post("/", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = get_password_hash(user.password)
    new_user = User(username=user.username, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
