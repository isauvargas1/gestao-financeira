# backend/app/schemas/investimento.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class InvestimentoCreate(BaseModel):
    carteira: str
    descricao: Optional[str] = None

class InvestimentoUpdate(BaseModel):
    carteira: Optional[str] = None
    descricao: Optional[str] = None

class InvestimentoRead(BaseModel):
    id: int
    usuario_id: int
    carteira: str
    descricao: Optional[str]
    valor_total: float
    data_criacao: datetime

    class Config:
        from_attributes = True
