# backend/app/models/movimentacao_investimento.py
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, CheckConstraint
from datetime import datetime
from app.core.database import Base

class MovimentacaoInvestimento(Base):
    __tablename__ = "movimentacoes_investimentos"

    id = Column(Integer, primary_key=True, index=True)
    investimento_id = Column(
        Integer,
        ForeignKey("investimentos.id", ondelete="CASCADE"),
        nullable=False
    )
    tipo = Column(String(10), nullable=False)  # 'aporte' ou 'resgate'
    valor = Column(Numeric(14, 2), nullable=False)
    data = Column(DateTime, default=datetime.utcnow, nullable=False)
    descricao = Column(String, nullable=True)

    __table_args__ = (
        CheckConstraint("tipo IN ('aporte','resgate')", name="ck_mov_tipo"),
    )
