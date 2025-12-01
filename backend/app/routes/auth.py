from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import User
from app.config import settings

router = APIRouter()

@router.post("/register")
def register_user(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = User(username=form_data.username, email=form_data.username, password_hash=form_data.password, role="user")
    db.add(user)
    db.commit()
    db.close()
    return {"user_id": user.user_id, "username": user.username, "email": user.email, "role": user.role}

@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not user.password_hash == form_data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = jwt.encode({"sub": user.username, "exp": datetime.utcnow() + access_token_expires}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    db.close()
    return {"access_token": access_token, "token_type": "bearer"}