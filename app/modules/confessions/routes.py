from fastapi import APIRouter

confession_router = APIRouter(
    prefix='/v1/router',
    tags=["confession"]
)

@confession_router.get('/', status_code=200)
def test_route():
    return {"Message" : "Success"}