# backend/app/services/receita_service.py
from sqlalchemy.orm import Session
from app.models.receita import Receita
from app.schemas.receita import ReceitaCreate, ReceitaUpdate

def get_receitas(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Receita).filter(Receita.usuario_id == user_id).offset(skip).limit(limit).all()

def get_receita(db: Session, user_id: int, receita_id: int):
    return db.query(Receita).filter(
        Receita.usuario_id == user_id,
        Receita.id == receita_id
    ).first()

def create_receita(db: Session, user_id: int, receita: ReceitaCreate):
    db_rec = Receita(**receita.dict(), usuario_id=user_id)
    db.add(db_rec)
    db.commit()
    db.refresh(db_rec)
    return db_rec

def update_receita(db: Session, existing: Receita, updates: ReceitaUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(existing, field, value)
    db.commit()
    db.refresh(existing)
    return existing

def delete_receita(db: Session, existing: Receita):
    db.delete(existing)
    db.commit()
