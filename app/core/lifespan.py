from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.dependencies import get_container

@asynccontextmanager
async def lifespan(app: FastAPI):
    container = get_container()

    app.state.user_service = container.user_service

    print("[SERVER] Sistema inicializado e dependências injetadas.")
    yield
    print("[SERVER] Encerrando sistema...")
