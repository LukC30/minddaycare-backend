from pydantic import BaseModel

class ConfessionModel(BaseModel):
    id: int
    id_user: int
    humor: str
    descricao: str
    created_at: str

    def to_insert(self):
        insert_data = self.model_dump().values()
        return insert_data