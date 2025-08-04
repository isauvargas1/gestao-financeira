# backend/app/schemas/movimentacao_investimento.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MovimentacaoInvestimentoCreate(BaseModel):
    tipo: str             # 'aporte' ou 'resgate'
    valor: float
    data: Optional[datetime] = None
    descricao: Optional[str] = None

class MovimentacaoInvestimentoUpdate(BaseModel):
    tipo: Optional[str] = None
    valor: Optional[float] = None
    data: Optional[datetime] = None
    descricao: Optional[str] = None

class MovimentacaoInvestimentoRead(BaseModel):
    id: int
    investimento_id: int
    tipo: str
    valor: float
    data: datetime
    descricao: Optional[str]

    class Config:
        from_attributes = True
