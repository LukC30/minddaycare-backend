from fastapi import APIRouter, Request
from .schema import UserRequestDTO
router = APIRouter(
    prefix='/v1',
    tags=['Main data']
)

@router.get('/test', status_code=200)
def test_route():
    return {"Message":"Success"}

@router.post('/', status_code=200)
async def create_user(user: UserRequestDTO, request: Request):
    user_service = request.app.state.service
    try:
        user_service.create_user(user)
    except Exception as e:
        return {"Error":f"{e}"}
    
    return {"Message":"Success"}