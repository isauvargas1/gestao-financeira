# backend/app/schemas/receita.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReceitaCreate(BaseModel):
    tipo_receita: str
    descricao_origem: str
    valor: float
    data_recebimento: Optional[datetime] = None

class ReceitaUpdate(BaseModel):
    tipo_receita: Optional[str] = None
    descricao_origem: Optional[str] = None
    valor: Optional[float] = None
    data_recebimento: Optional[datetime] = None

class ReceitaRead(BaseModel):
    id: int
    usuario_id: int
    tipo_receita: str
    descricao_origem: str
    valor: float
    data_recebimento: Optional[datetime]
    data_criacao: datetime

    class Config:
        from_attributes = True
