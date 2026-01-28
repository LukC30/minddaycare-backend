from fastapi import APIRouter, Request, Depends, Response
from starlette.status import HTTP_404_NOT_FOUND
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
def create_user(user: UserRequestDTO, user_service: UserService = Depends(get_user_service)):
    #meu deus que frescura, eu juro que nao foi IA q fez isso
    #o codigo esta tao porco quanto eu faria

    try:
        user_service.create_user(user)
        return {"message" : "success"}
    except Exception as e:
        return {"error":f"{e}"}


@user_router.get('/all-users', status_code=200)
def get_users(response: Response, user_service: UserService = Depends(get_user_service)):
    users = user_service.get_all_users()
    if not users:
        response.status_code = HTTP_404_NOT_FOUND
    return {"users": user_service.get_all_users()}


@user_router.get('/{id}')
def get_user_by_id(id: int, response: Response, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user(id)
    if not user:
        response.status_code = HTTP_404_NOT_FOUND
    
    return {"user": user}
    
@user_router.get('/{email}')
def get_user_by_email(email: str, response: Response, user_service: UserService = Depends(get_user_service)):
    user = user_service.get_user_by_email(email)
    if not user:
        response.status_code = HTTP_404_NOT_FOUND
    
    return {"user": user}


@user_router.put('/')
def update_user(user_request: UserRequestDTO, user_service: UserService = Depends(get_user_service)):

    user_updated = user_service.update_user(user_request)
    return {"message":"success", "user" : user_updated}

@user_router.delete('/')
def delete_user(user_request: UserRequestDTO, user_service: UserService = Depends(get_user_service)):
    user_service.delete(user_request)
    return {"message": "success"}

