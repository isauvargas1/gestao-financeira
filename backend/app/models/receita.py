# backend/app/models/receita.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from app.core.database import Base

class Receita(Base):
    __tablename__ = "receitas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo_receita = Column(String, nullable=False)
    descricao_origem = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    data_recebimento = Column(DateTime, nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
