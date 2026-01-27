from .interface import BaseAuthRepository
from .model import AuthModel
from .mapper import AuthMapper
from datetime import datetime

class AuthRepository(BaseAuthRepository):
    def __init__(self, db):
        super().__init__(db)

    def create(self, auth_model: AuthModel):
        sql = "INSERT INTO tbl_refresh_token(id_user, token_hash, created_at, expires_at) VALUES(%s, %s, %s, %s)"
        data_insert = AuthMapper.model_to_tuple(auth_model)
        print(data_insert)
        with self.db.alter_cursor() as c:
            c.execute(sql, data_insert)
        
        return True
    
    def select_by_date(self, date: datetime, id_user: int):
        sql = "SELECT * FROM tbl_refresh_token WHERE id_user = %s AND expires_at > %s"
        with self.db.read_cursor() as c:
            c.execute(sql, (id_user, date))
            data = c.fetchall()
            
        return data
    
