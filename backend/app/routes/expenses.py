# backend/app/routes/expenses.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.expense import DespesaCreate, DespesaRead, DespesaUpdate
from app.services.expense_service import (
    get_despesas, get_despesa,
    create_despesa, update_despesa, delete_despesa
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/despesas", tags=["despesas"])

@router.get("/", response_model=List[DespesaRead])
def read_despesas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_despesas(db, current_user.id, skip, limit)

@router.post(
    "/", response_model=DespesaRead, status_code=status.HTTP_201_CREATED
)
def create_new_despesa(
    despesa: DespesaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_despesa(db, current_user.id, despesa)

@router.get("/{despesa_id}", response_model=DespesaRead)
def read_despesa(
    despesa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_despesa = get_despesa(db, current_user.id, despesa_id)
    if not db_despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    return db_despesa

@router.put("/{despesa_id}", response_model=DespesaRead)
def update_existing_despesa(
    despesa_id: int,
    updates: DespesaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_despesa = get_despesa(db, current_user.id, despesa_id)
    if not db_despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    return update_despesa(db, db_despesa, updates)

@router.delete("/{despesa_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_despesa(
    despesa_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_despesa = get_despesa(db, current_user.id, despesa_id)
    if not db_despesa:
        raise HTTPException(status_code=404, detail="Despesa não encontrada")
    delete_despesa(db, db_despesa)
    return
