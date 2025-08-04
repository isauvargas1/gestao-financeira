# backend/drop_users_table.py
from sqlalchemy import text
from app.core.database import engine

# Abre uma transação e executa o SQL
with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS users;"))

print("Tabela 'users' removida com sucesso!")
