from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker
from app.models import Base

engine = create_engine('sqlite:///app.db')
Base.metadata.create_all(engine)

def get_db():
    db = scoped_session(sessionmaker(bind=engine))
    try:
        yield db
    finally:
        db.close()