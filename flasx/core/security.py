from passlib.context import CryptContext  
from jose import jwt  
from datetime import datetime, timedelta  
from flasx.core.config import settings  

# Set up the password hashing context using bcrypt algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"  # JWT signing algorithm

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)): # Create a JWT token with an expiration time
    to_encode = data.copy()  
    to_encode.update({"exp": datetime.utcnow() + expires_delta})  
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM) # Encode the token with the SECRET_KEY and algorithm, then return it
