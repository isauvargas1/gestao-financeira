# backend/app/routes/receitas.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.receita import ReceitaCreate, ReceitaRead, ReceitaUpdate
from app.services.receita_service import (
    get_receitas, get_receita,
    create_receita, update_receita, delete_receita
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/receitas", tags=["receitas"])

@router.get("/", response_model=List[ReceitaRead])
def read_receitas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_receitas(db, current_user.id, skip, limit)

@router.post("/", response_model=ReceitaRead, status_code=status.HTTP_201_CREATED)
def create_new_receita(
    receita: ReceitaCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_receita(db, current_user.id, receita)

@router.get("/{receita_id}", response_model=ReceitaRead)
def read_receita(
    receita_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_rec = get_receita(db, current_user.id, receita_id)
    if not db_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    return db_rec

@router.put("/{receita_id}", response_model=ReceitaRead)
def update_existing_receita(
    receita_id: int,
    updates: ReceitaUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_rec = get_receita(db, current_user.id, receita_id)
    if not db_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    return update_receita(db, db_rec, updates)

@router.delete("/{receita_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_receita(
    receita_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    db_rec = get_receita(db, current_user.id, receita_id)
    if not db_rec:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Receita não encontrada")
    delete_receita(db, db_rec)
    return
