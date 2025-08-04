# backend/app/schemas/expense.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DespesaCreate(BaseModel):
    tipo_despesa: str
    categoria: str
    produto_servico: str
    forma_pagamento: str
    valor: float
    data_pagamento: Optional[datetime] = None
    is_data_vencimento: bool = False

class DespesaUpdate(BaseModel):
    tipo_despesa: Optional[str] = None
    categoria: Optional[str] = None
    produto_servico: Optional[str] = None
    forma_pagamento: Optional[str] = None
    valor: Optional[float] = None
    status_pagamento: Optional[bool] = None
    data_pagamento: Optional[datetime] = None
    is_data_vencimento: Optional[bool] = None


class DespesaRead(BaseModel):
    id: int
    usuario_id: int
    tipo_despesa: str
    categoria: str
    produto_servico: str
    forma_pagamento: str
    valor: float
    status_pagamento: bool
    data_criacao: datetime
    data_pagamento: Optional[datetime]
    is_data_vencimento: bool
    status_divida: str

    class Config:
        from_attributes = True
