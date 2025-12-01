from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from pydantic import BaseModel
from app.models import User
from app.config import settings
from datetime import datetime, timedelta
from jose import jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def authenticate_user(username: str, password: str):
    # authenticate user logic
    return User()

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm='HS256')
    return encoded_jwt