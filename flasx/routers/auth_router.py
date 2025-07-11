from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from flasx.database import get_db
from flasx.models.user_model import User
from flasx.core.security import verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first() # Query the database to find a user by username
    if not user or not verify_password(form_data.password, user.hashed_password): # Check if user exists and password is correct
        raise HTTPException(status_code=400, detail="Incorrect credentials")
    token = create_access_token({"sub": user.username}) #  Create a JWT access token 
    return {"access_token": token, "token_type": "bearer"}
