from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.dependencies import get_container
from .dependencies import db_instance

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("[SERVER] Sistema inicializado e dependências injetadas.")
    yield
    print("[SERVER] Encerrando sistema...")
