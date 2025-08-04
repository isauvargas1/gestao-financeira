# backend/app/services/movimentacao_investimento_service.py
from sqlalchemy.orm import Session
from app.models.movimentacao_investimento import MovimentacaoInvestimento
from app.schemas.movimentacao_investimento import (
    MovimentacaoInvestimentoCreate,
    MovimentacaoInvestimentoUpdate,
)
from app.services.investimento_service import recalc_valor_total

def get_movimentacoes(
    db: Session, investimento_id: int, skip: int = 0, limit: int = 100
):
    return (
        db.query(MovimentacaoInvestimento)
          .filter(MovimentacaoInvestimento.investimento_id == investimento_id)
          .offset(skip)
          .limit(limit)
          .all()
    )

def get_movimentacao(
    db: Session, investimento_id: int, mov_id: int
):
    return (
        db.query(MovimentacaoInvestimento)
          .filter(
              MovimentacaoInvestimento.investimento_id == investimento_id,
              MovimentacaoInvestimento.id == mov_id
          )
          .first()
    )

def create_movimentacao(
    db: Session, investimento_id: int, mov_data: MovimentacaoInvestimentoCreate
):
    mov = MovimentacaoInvestimento(
        investimento_id=investimento_id,
        **mov_data.dict()
    )
    db.add(mov)
    db.commit()
    db.refresh(mov)
    # Recalcula valor_total do investimento após o aporte ou resgate
    recalc_valor_total(db, investimento_id)
    return mov

def update_movimentacao(
    db: Session, mov: MovimentacaoInvestimento, updates: MovimentacaoInvestimentoUpdate
):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(mov, field, value)
    db.commit()
    db.refresh(mov)
    recalc_valor_total(db, mov.investimento_id)
    return mov

def delete_movimentacao(
    db: Session, mov: MovimentacaoInvestimento
):
    inv_id = mov.investimento_id
    db.delete(mov)
    db.commit()
    # Recalcula valor_total após exclusão da movimentação
    recalc_valor_total(db, inv_id)
