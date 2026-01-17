from pydantic import BaseModel

class ConfessionModel(BaseModel):
    id: int
    id_user: int
    humor: str
    descricao: str
    created_at: str

