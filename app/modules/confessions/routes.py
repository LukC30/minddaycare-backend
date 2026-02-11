from fastapi import APIRouter
from .schemas import ConfessionRequestDTO
from app.modules.auth.routes import get_current_user
from app.core.dependencies import get_confession_service


confession_router = APIRouter(
    prefix='/v1/router',
    tags=["confession"]
)

@confession_router.get('/', status_code=200)
def test_route():
    return {"Message" : "Success"}


def create_confession():