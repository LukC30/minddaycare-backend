from .interface import BaseConfessionRepository
from .models import ConfessionModel
from .mapper import ConfessionMapper

class ConfessionRepository(BaseConfessionRepository):
    def __init__(self, db):
        super().__init__(db)


    def create(self, confession_create: ConfessionModel):
        insert_data = ConfessionMapper.to_insert(confession_create)
        
        with self.db.alter_cursor() as c:
            sql = "INSERT INTO tbl_desabafo(id_user, humor, descricao) VALUES(%s, %s, %s)"
            c.execute(sql, insert_data)
            return confession_create
    
        return None
        
