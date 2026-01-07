from fastapi import APIRouter, Request
from app.schemas import UserDTO
router = APIRouter(
    prefix='/v1',
    tags=['Main data']
)


@router.get('/test', status_code=200)
def test_route():
    return {"Message":"Success"}

@router.post('/', status_code=200)
async def create_user(user: UserDTO, request: Request):
    service = request.app.state.service
    try:
        service.create_user(user)
    except Exception as e:
        return {"Error":f"{e}"}
    
    return {"Message":"Success"}