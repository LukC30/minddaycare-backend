from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv

from .config import get_database_env
from .dependencies import db_instance

@asynccontextmanager
async def lifespan(app: FastAPI):

    load_dotenv()
    print("[SERVER] Sistema inicializado e dependências injetadas.")
    db_instance.connection(get_database_env())
    yield
    db_instance.disconnect()
    print("[SERVER] Encerrando sistema...")
