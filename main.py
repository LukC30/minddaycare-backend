from fastapi import FastAPI
from app.database.db import Database
from app.repository import UserRepository
from app.routes import router
import logging
import uvicorn

from app.services import UserService

logging.basicConfig(format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',)
logger = logging.getLogger(__name__)
app = FastAPI(
    title="MindDayCare",
    description="Para cuidar da cabecinha hehehe",
)
db = Database()
user_repo = UserRepository(db)
user_service = UserService(user_repo)

app.include_router(router)
app.state.service = user_service

@app.get('/')
def test_route():
    return {"message" : "rodando vrumvrum"}

if __name__ == "__main__":
    uvicorn.run(app=app, log_level="debug")
