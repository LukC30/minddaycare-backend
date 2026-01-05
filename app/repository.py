from app.database.db import Database
from app.schemas import UserDTO
from app.models import UserModel
import logging

logger = logging.getLogger(__name__)

class UserRepository():
    def __init__(self, db: Database):
        self.db = db

    async def create_user(self, user_data: UserDTO):
        user_model= UserModel(**user_data.model_dump().copy())
        insert_data = user_model.to_insert()
        logger.info("Trying to insert data.")
        with self.db.alter_cursor() as c:
            sql = "INSERT INTO tbl_users(nome, email, senha, telefone) VALUES (?, ?, ?, ?)"
            await c.execute(sql, insert_data)
        return 



