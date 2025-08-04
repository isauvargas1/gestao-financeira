# backend/app/models/expense.py
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime, date
from app.core.database import Base

class Despesa(Base):
    __tablename__ = "despesas"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    tipo_despesa = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    produto_servico = Column(String, nullable=False)
    forma_pagamento = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    status_pagamento = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    # Novas colunas
    data_pagamento = Column(DateTime, nullable=True)
    is_data_vencimento = Column(Boolean, default=False)

    @hybrid_property
    def status_divida(self) -> str:
        # Já pago
        if self.status_pagamento:
            return "pago"

        # Sem data definida
        if not self.data_pagamento:
            return "aguardando pagamento"

        today = date.today()
        target = self.data_pagamento.date()

        if self.is_data_vencimento:
            diff = (target - today).days
            if diff < 0:
                return "atrasada"
            if diff == 0:
                return "vence hoje"
            if diff == 1:
                return "vence amanhã"
            if diff <= 5:
                return f"vence em {diff} dias"
            return "dentro do prazo"

        # Data de pagamento informada, mas não é vencimento
        return "aguardando pagamento"
