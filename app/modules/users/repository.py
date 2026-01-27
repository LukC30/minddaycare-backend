from .interfaces import BaseUserRepository
from .model import UserModel
from .mapper import UserMapper
import logging
from typing import Union
logger = logging.getLogger(__name__)


class UserRepository(BaseUserRepository):
    def __init__(self, db):
        super().__init__(db)

    def create(self, user_model: UserModel):
        if not user_model:
            return None

        insert_data = UserMapper.to_insert(user_model)
        print(insert_data)
        with self.db.alter_cursor() as c:
            sql = "INSERT INTO tbl_users (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)"
            c.execute(sql, insert_data)
            return user_model
        
        return None
    
    def get_all(self):
        users = []
        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users WHERE is_active = '1'"
            c.execute(sql)
            users_data = c.fetchall()

        if not users_data:
            return []

        users = UserMapper.to_user_model_list(users_data)
        return users
    
    def get_by_id(self, id):
        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users WHERE id = %s AND is_active='1'"
            logger.info(sql)
            c.execute(sql, (id,))
            user = c.fetchone()
        
        if not user:
            return None

        user_model = UserMapper.to_model(user)
        return user_model
    
    def get_by_email(self, email) -> Union[UserModel, None]:
        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users WHERE email = %s AND is_active = '1'"
            c.execute(sql, (email,))
            user = c.fetchone()

        if not user:
            return None
        user_model = UserMapper.to_model(user)
        return user_model
    
    def update(self, user_request: UserModel) -> Union[dict, None]:
        with self.db.alter_cursor() as c:
            user_insert = user_request.model_dump()
            sql = """
                UPDATE tbl_users 
                SET nome = %(nome)s, 
                    senha = %(senha)s, 
                    telefone = %(telefone)s 
                WHERE email = %(email)s 
                AND is_active=1
            """
            c.execute(sql, user_insert)
            return user_request.model_dump()
        
        return None
        
    
    def delete(self, user_request: UserModel):
        with self.db.alter_cursor() as c:
            sql = "UPDATE FROM tbl_users SET is_active=0 WHERE email = '%s'"
            to_insert = UserMapper.to_insert(user_request)
            c.execute(sql, to_insert)

        return True

