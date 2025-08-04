# backend/app/services/expense_service.py
from sqlalchemy.orm import Session
from app.models.expense import Despesa
from app.schemas.expense import DespesaCreate, DespesaUpdate

def get_despesas(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Despesa).filter(Despesa.usuario_id == user_id).offset(skip).limit(limit).all()

def get_despesa(db: Session, user_id: int, despesa_id: int):
    return db.query(Despesa).filter(
        Despesa.usuario_id == user_id, Despesa.id == despesa_id
    ).first()

def create_despesa(db: Session, user_id: int, despesa: DespesaCreate):
    db_despesa = Despesa(**despesa.dict(), usuario_id=user_id)
    db.add(db_despesa)
    db.commit()
    db.refresh(db_despesa)
    return db_despesa

def update_despesa(db: Session, existing: Despesa, updates: DespesaUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(existing, field, value)
    db.commit()
    db.refresh(existing)
    return existing

def delete_despesa(db: Session, existing: Despesa):
    db.delete(existing)
    db.commit()
