from app.database.db import Database
from app.schemas import UserDTO
from app.models import UserModel
import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

class BaseRepository(ABC):
    def __init__(self, db: Database):
        self.db = db

class UserRepository(BaseRepository):

    def create_user(self, user_data: UserDTO):
        user_model= UserModel(**user_data.model_dump().copy())
        insert_data = user_model.to_insert()
        logger.info("Trying to insert data.")
        with self.db.alter_cursor() as c:
            sql = "INSERT INTO tbl_users (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)"
            c.execute(sql, insert_data)
        return 



