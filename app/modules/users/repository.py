from .interfaces import BaseUserRepository
from .schema import UserRequestDTO
from .model import UserModel
from .mapper import UserMapper
import logging
logger = logging.getLogger(__name__)


class UserRepository(BaseUserRepository):
    def __init__(self, db):
        super().__init__(db)

    def create(self, user_model: UserModel):
        insert_data = UserMapper.to_insert(user_model)
        with self.db.alter_cursor() as c:
            sql = "INSERT INTO tbl_users (nome, email, senha, telefone) VALUES (%s, %s, %s, %s)"
            c.execute(sql, insert_data)
        return 
    
    def get_all(self):
        users = []

        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users"
            c.execute(sql)
            users_data = c.fetchall()
        
        print(users_data)
        users = UserMapper.to_user_model_list(users_data)
        print(users)
        return users
    
    def get_by_id(self, id):
        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users WHERE id = %s"
            logger.info(sql)
            c.execute(sql, (id,))
            user = c.fetchone()

        user_model = UserMapper.to_model(user)
        return user_model
    
    def get_by_email(self, user_request: UserRequestDTO):
        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users WHERE email = %s"
            c.execute(sql, (user_request.email,))
            user = c.fetchone()

        user_model = UserMapper.to_model(user)
        return user_model
    
    def update(self, user_request: UserRequestDTO):
        with self.db.read_cursor() as c:
            sql = "UPDATE FROM tbl_users set(name, email, senha, telefone) WHERE email = '%s'", user_request.email
            to_insert = UserMapper.to_insert(user_request)
            c.execute(sql, to_insert)
        
        user_response = UserMapper.to_user_response_schema(user_request)
        return user_response
    
    def delete(self, user_request: UserRequestDTO):
        return 

