# backend/app/services/investimento_service.py
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.investimento import Investimento
from app.models.movimentacao_investimento import MovimentacaoInvestimento
from app.schemas.investimento import InvestimentoCreate, InvestimentoUpdate

def get_investimentos(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(Investimento)
          .filter(Investimento.usuario_id == user_id)
          .offset(skip)
          .limit(limit)
          .all()
    )

def get_investimento(db: Session, user_id: int, investimento_id: int):
    return (
        db.query(Investimento)
          .filter(Investimento.usuario_id == user_id, Investimento.id == investimento_id)
          .first()
    )

def create_investimento(db: Session, user_id: int, inv_data: InvestimentoCreate):
    inv = Investimento(usuario_id=user_id, carteira=inv_data.carteira, descricao=inv_data.descricao)
    db.add(inv)
    db.commit()
    db.refresh(inv)
    return inv

def update_investimento(db: Session, existing: Investimento, updates: InvestimentoUpdate):
    for field, value in updates.dict(exclude_unset=True).items():
        setattr(existing, field, value)
    db.commit()
    db.refresh(existing)
    return existing

def delete_investimento(db: Session, existing: Investimento):
    db.delete(existing)
    db.commit()

def recalc_valor_total(db: Session, investimento_id: int):
    """
    Recalcula valor_total = soma(aportes) - soma(resgates)
    e atualiza o campo no registro de Investimento.
    """
    total_aportes = db.query(
        func.coalesce(func.sum(MovimentacaoInvestimento.valor), 0)
    ).filter(
        MovimentacaoInvestimento.investimento_id == investimento_id,
        MovimentacaoInvestimento.tipo == "aporte"
    ).scalar()

    total_resgates = db.query(
        func.coalesce(func.sum(MovimentacaoInvestimento.valor), 0)
    ).filter(
        MovimentacaoInvestimento.investimento_id == investimento_id,
        MovimentacaoInvestimento.tipo == "resgate"
    ).scalar()

    novo_total = total_aportes - total_resgates
    investimento = db.query(Investimento).get(investimento_id)
    investimento.valor_total = novo_total
    db.commit()
    db.refresh(investimento)
    return investimento
