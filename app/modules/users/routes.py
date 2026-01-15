from fastapi import APIRouter, Request, Depends
from app.core.dependencies import get_user_service
from .schema import UserRequestDTO
from .service import UserService

user_router = APIRouter(
    prefix='/v1/user',
    tags=['Main data']
)

@user_router.get('/test', status_code=200)
def test_route():
    return {"Message":"Success"}

@user_router.post('/', status_code=201)
async def create_user(user: UserRequestDTO, user_service: UserService = Depends(get_user_service)):
    #meu deus que frescura, eu juro que nao foi IA q fez isso
    #o codigo esta tao porco quanto eu faria

    try:
        user_service.create_user(user)
        return {"message" : "success"}
    except Exception as e:
        return {"error":f"{e}"}

@user_router.get('/all-users', status_code=200)
async def get_users(user_service: UserService = Depends(get_user_service)):

    try:
        return {"users": user_service.get_all_users()}
    except Exception as e:
        return {"error":f"{e}"}
    
@user_router.get('/{id}')
def get_user(id: int, user_service: UserService = Depends(get_user_service)):

    try:
        user = user_service.get_user(id)
        return {'user' : user}
    
    except Exception as e:
        return {"error":f"{e}"}

@user_router.put('/')
def update_user(user_request: UserRequestDTO, user_service: UserService = Depends(get_user_service)):

    try:
        user_service.update_user(user_request)
        return {"message":"success", "user" : {user_service}}
    except Exception as e:
        return {"error":f"{e}"}

@user_router.delete('/')
def delete_user(user_request: UserRequestDTO, user_service: UserService = Depends(get_user_service)):
    try:
        user_service.delete(user_request)
        return {"message": "sucess"}
    except Exception as e:
        return {"error":f"{e}"}
