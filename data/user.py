from sqlalchemy.orm import Session
from schema.user import UserBase, UserCreate
from errors import Missing, Duplicate
from model.user import User


def get_all(db: Session) -> list[User]:
    return db.query(User).all()


def get_one(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise Missing("User not found")
    return user


def create(db: Session, user: UserCreate) -> User:
    if db.query(User).filter(User.username == user.username).first():
        raise Duplicate("Username already exists")
    if db.query(User).filter(User.email == user.email).first():
        raise Duplicate("Email already exists")
    user = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update(db: Session, user: User):
    db.query(User).filter(User.id == user.id).update({User: user})
    db.commit()
    return db.query(User).filter(User.id == user.id).first()


def delete(db: Session, user_id: int):
    db.query(User).filter(User.id == user_id).delete()
    db.commit()
    return True
