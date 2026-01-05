from fastapi import APIRouter
from app.schemas import UserDTO
from app.database.db import Database
from app.repository import UserRepository
from app.services import UserService

router = APIRouter(
    prefix='/v1',
    tags=['Main data']
)

db = Database()
user_repo = UserRepository(db)
user_service = UserService(user_repo)

@router.get('/test', status_code=200)
def test_route():
    return {"Message":"Success"}

@router.post('/', status_code=200)
async def create_user(user: UserDTO):
    try:
        await user_service.create_user(user)
    except Exception as e:
        return {"Error":f"{e}"}
    
    return {"Message":"Success"}