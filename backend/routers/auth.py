from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session  
from database import get_db
from models.users import User
from utils.security import hash_password,verify_password
from schemas.users import UserCreate, UserResponse


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    exiting_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if exiting_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    hashed_password = hash_password(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=UserResponse)
def login(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.username == user.username) | (User.email == user.email)).first()
    if not existing_user or not verify_password(user.password, existing_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    return existing_user 