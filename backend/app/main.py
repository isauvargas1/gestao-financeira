from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

# Criação das tabelas
from app.core.database import engine, Base
import app.models.user
import app.models.expense
import app.models.receita
import app.models.investimento
import app.models.movimentacao_investimento
Base.metadata.create_all(bind=engine)

from app.routes.auth import router as auth_router
from app.routes.expenses import router as expenses_router
from app.routes.receitas import router as receitas_router
from app.routes.investimentos import router as investimentos_router   # <-- adicionado
from app.routes.movimentacoes_investimento import router as mov_invest_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(expenses_router)
app.include_router(receitas_router)
app.include_router(investimentos_router)     # <-- adicionado
app.include_router(mov_invest_router)

@app.get("/")
async def root():
    return {"message": "API está no ar!"}
