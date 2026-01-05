from fastapi import FastAPI
from app.routes import router
import logging
import uvicorn

logging.basicConfig(format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="MindDayCare",
    description="Para cuidar da cabecinha hehehe",
)

app.include_router(router)

@app.get('/')
def test_route():
    return {"message" : "rodando vrumvrum"}

if __name__ == "__main__":
    uvicorn.run(app=app, log_level="debug")
