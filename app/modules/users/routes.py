from fastapi import APIRouter, Request
from .schema import UserRequestDTO
from .service import UserService
user_router = APIRouter(
    prefix='/v1/user',
    tags=['Main data']
)

def _get_service(request: Request):
    user_service: UserService = request.app.state.user_service
    return user_service

@user_router.get('/test', status_code=200)
def test_route():
    return {"Message":"Success"}

@user_router.post('/', status_code=201)
async def create_user(user: UserRequestDTO, request: Request):
    #meu deus que frescura, eu juro que nao foi IA q fez isso
    #o codigo esta tao porco quanto eu faria
    user_service = _get_service(request)

    try:
        user_service.create_user(user)
        return {"message" : "success"}
    except Exception as e:
        return {"error":f"{e}"}

@user_router.get('/all-users', status_code=200)
async def get_users(request: Request):
    user_service = _get_service(request)

    try:
        return {"users": user_service.get_all_users()}
    except Exception as e:
        return {"error":f"{e}"}
    
@user_router.get('/{id}')
def get_user(id: int, request: Request):
    user_service = _get_service(request)

    try:
        user = user_service.get_user(id)
        return {'user' : user}
    
    except Exception as e:
        return {"error":f"{e}"}

@user_router.put('/')
def update_user(user_request: UserRequestDTO, request: Request):
    user_service = _get_service(request)

    try:
        user_service.update_user(user_request)
        return {"message":"success", "user" : {user_service}}
    except Exception as e:
        return {"error":f"{e}"}
