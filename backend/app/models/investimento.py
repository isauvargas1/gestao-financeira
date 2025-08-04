# backend/app/models/investimento.py
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Investimento(Base):
    __tablename__ = "investimentos"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    carteira = Column(String(100), nullable=False)
    descricao = Column(String, nullable=True)
    valor_total = Column(Numeric(14, 2), nullable=False, default=0)
    data_criacao = Column(DateTime, default=datetime.utcnow, nullable=False)
