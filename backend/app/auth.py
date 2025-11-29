from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import get_session
from app.models import User
from jose import jwt
from passlib.context import CryptContext
router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str

class PasswordResetRequest(BaseModel):
    email: str
    new_password: str

crypt = CryptContext(schemes=['bcrypt'], default='bcrypt')
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@router.post('/login')
def login(request: LoginRequest):
    session = get_session()
    user = session.query(User).filter_by(email=request.email).first()
    if not user:
        raise HTTPException(status_code=401, detail='Invalid email or password')
    if not crypt.verify(request.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid email or password')
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={'sub': user.email}, expires_delta=access_token_expires)
    return {'access_token': access_token, 'token_type': 'bearer'}