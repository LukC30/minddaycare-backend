from fastapi import APIRouter, Request
from .schema import UserRequestDTO
from .service import UserService
user_router = APIRouter(
    prefix='/v1/user',
    tags=['Main data']
)

@user_router.get('/test', status_code=200)
def test_route():
    return {"Message":"Success"}

@user_router.post('/', status_code=200)
async def create_user(user: UserRequestDTO, request: Request):
    #meu deus que frescura, eu juro que nao foi IA q fez isso
    #o codigo esta tao porco quanto eu faria
    user_service: UserService = request.app.state.user_service

    try:
        user_service.create_user(user)
    except Exception as e:
        return {"Error":f"{e}"}
    
    return {"Message":"Success"}

@user_router.get('/all-users', status_code=200)
async def get_users(request: Request):
    user_service: UserService = request.app.state.user_service

    try:
        return {"users": user_service.get_all_users()}
    except Exception as e:
        return {"Error":f"{e}"}
    
@user_router.get('/{id}')
def get_user(id: int, request: Request):
    user_service: UserService = request.app.state.user_service

    try:
        user = user_service.get_user(id)
        return {'user' : user}
    
    except Exception as e:
        return {"Error":f"{e}"}