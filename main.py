#internal imports
from app.core.lifespan import lifespan
from app.core.config import setup_logging
from app.modules.users.routes import user_router
from app.modules.auth.routes import auth_router

#external imports
from fastapi import FastAPI
import logging
import uvicorn

logging.basicConfig(format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',)
logger = logging.getLogger(__name__)
app = FastAPI(
    title="MindDayCare",
    description="Para cuidar da cabecinha hehehe",
    lifespan=lifespan
)

app.include_router(user_router)

@app.get('/')
def test_route():
    return {"message" : "rodando vrumvrum"}

if __name__ == "__main__":
    setup_logging()
    uvicorn.run(app="main:app", reload=True)