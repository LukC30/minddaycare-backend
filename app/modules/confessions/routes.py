from fastapi import APIRouter, Depends

from app.modules.auth.routes import get_current_user
from app.core.dependencies import get_confession_service
from app.modules.auth.routes import get_current_user

from .schemas import ConfessionRequestDTO
from .service import ConfessionService

confession_router = APIRouter(
    prefix='/v1/router',
    tags=["confession"]
)

@confession_router.get('/', status_code=200)
def test_route():
    return {"Message" : "Success"}

@confession_router.post('/create')
def create_confession(confession_request: ConfessionRequestDTO,
                      access_token = Depends(get_current_user), 
                      confession_service: ConfessionService = Depends(get_confession_service)):
    # eu odeio deixar identado assim
    confession_data = confession_service.create(confession_request, access_token)
    return confession_data
