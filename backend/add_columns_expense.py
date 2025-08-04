# backend/add_columns_expense.py
from sqlalchemy import text
from app.core.database import engine

with engine.begin() as conn:
    conn.execute(text("ALTER TABLE despesas ADD COLUMN IF NOT EXISTS data_pagamento TIMESTAMP;"))
    conn.execute(text("ALTER TABLE despesas ADD COLUMN IF NOT EXISTS is_data_vencimento BOOLEAN DEFAULT FALSE;"))
print("Colunas adicionadas com sucesso!")
