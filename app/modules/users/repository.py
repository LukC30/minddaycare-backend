from .interfaces import BaseUserRepository
from .schema import UserRequestDTO
from .model import UserModel
from .mapper import UserMapper

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
            users_data:list[tuple] = c.fetchall()
        
        users = UserMapper.to_user_model_list(users_data)
        print(users)
        return users
    
    def get_by_id(self, id):
        with self.db.read_cursor() as c:
            sql = "SELECT * FROM tbl_users WHERE id = "+ str(id)
            c.execute(sql)
            user = c.fetchone()

        user_model = UserMapper.to_user_model(user)
        return user_model
    
    def update(self, user_request):
        return 
    
    def delete(self, id):
        return 

