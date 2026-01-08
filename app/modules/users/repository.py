from .interfaces import BaseUserRepository
from .schema import UserRequestDTO
from .model import UserModel
import logging

logger = logging.getLogger(__name__)

class UserRepository(BaseUserRepository):
    def __init__(self):
        super().__init__()

    def create_user(self, user_data: UserRequestDTO):
        user_model= UserModel(**user_data.model_dump().copy())
        insert_data = user_model.to_insert()
        logger.info("Trying to insert data.")
        with self.db.alter_cursor() as c:
            sql = "INSERT INTO tbl_users (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)"
            c.execute(sql, insert_data)
        return 
