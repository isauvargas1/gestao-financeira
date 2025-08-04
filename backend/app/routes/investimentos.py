# backend/app/routes/investimentos.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.investimento import (
    InvestimentoCreate,
    InvestimentoRead,
    InvestimentoUpdate,
)
from app.services.investimento_service import (
    get_investimentos,
    get_investimento,
    create_investimento,
    update_investimento,
    delete_investimento,
)
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(prefix="/investimentos", tags=["investimentos"])

@router.get("/", response_model=List[InvestimentoRead])
def read_investimentos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_investimentos(db, current_user.id, skip, limit)

@router.post(
    "/", response_model=InvestimentoRead, status_code=status.HTTP_201_CREATED
)
def create_new_investimento(
    inv_data: InvestimentoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_investimento(db, current_user.id, inv_data)

@router.get("/{investimento_id}", response_model=InvestimentoRead)
def read_investimento(
    investimento_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    inv = get_investimento(db, current_user.id, investimento_id)
    if not inv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investimento não encontrado",
        )
    return inv

@router.put("/{investimento_id}", response_model=InvestimentoRead)
def update_existing_investimento(
    investimento_id: int,
    updates: InvestimentoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    inv = get_investimento(db, current_user.id, investimento_id)
    if not inv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investimento não encontrado",
        )
    return update_investimento(db, inv, updates)

@router.delete("/{investimento_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_investimento(
    investimento_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    inv = get_investimento(db, current_user.id, investimento_id)
    if not inv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investimento não encontrado",
        )
    delete_investimento(db, inv)
    return
