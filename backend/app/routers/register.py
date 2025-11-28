from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import User
from app.database import get_db

router = APIRouter()

@router.post('/api/register')
def create_user(username: str, email: str, password: str, db: Session = Depends(get_db)):
    # Create user logic
    pass