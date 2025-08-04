# backend/app/routes/movimentacoes_investimento.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session

from app.schemas.movimentacao_investimento import (
    MovimentacaoInvestimentoCreate,
    MovimentacaoInvestimentoRead,
    MovimentacaoInvestimentoUpdate,
)
from app.services.movimentacao_investimento_service import (
    get_movimentacoes,
    get_movimentacao,
    create_movimentacao,
    update_movimentacao,
    delete_movimentacao,
)
from app.services.investimento_service import get_investimento
from app.core.database import get_db
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/investimentos/{investimento_id}/movimentacoes",
    tags=["movimentacoes_investimentos"],
)

def validate_investimento(
    investimento_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Garante que o investimento existe e pertence ao usuário logado.
    """
    inv = get_investimento(db, current_user.id, investimento_id)
    if not inv:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Investimento não encontrado",
        )
    return inv

@router.get("/", response_model=List[MovimentacaoInvestimentoRead])
def read_movimentacoes(
    investimento: any = Depends(validate_investimento),
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return get_movimentacoes(db, investimento.id, skip, limit)

@router.post(
    "/", response_model=MovimentacaoInvestimentoRead, status_code=status.HTTP_201_CREATED
)
def create_new_movimentacao(
    investimento: any = Depends(validate_investimento),
    mov_data: MovimentacaoInvestimentoCreate = None,
    db: Session = Depends(get_db),
):
    return create_movimentacao(db, investimento.id, mov_data)

@router.get("/{mov_id}", response_model=MovimentacaoInvestimentoRead)
def read_movimentacao(
    investimento: any = Depends(validate_investimento),
    mov_id: int = None,
    db: Session = Depends(get_db),
):
    mov = get_movimentacao(db, investimento.id, mov_id)
    if not mov:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimentação não encontrada",
        )
    return mov

@router.put("/{mov_id}", response_model=MovimentacaoInvestimentoRead)
def update_existing_movimentacao(
    investimento: any = Depends(validate_investimento),
    mov_id: int = None,
    updates: MovimentacaoInvestimentoUpdate = None,
    db: Session = Depends(get_db),
):
    mov = get_movimentacao(db, investimento.id, mov_id)
    if not mov:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimentação não encontrada",
        )
    return update_movimentacao(db, mov, updates)

@router.delete("/{mov_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_existing_movimentacao(
    investimento: any = Depends(validate_investimento),
    mov_id: int = None,
    db: Session = Depends(get_db),
):
    mov = get_movimentacao(db, investimento.id, mov_id)
    if not mov:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movimentação não encontrada",
        )
    delete_movimentacao(db, mov)
    return
