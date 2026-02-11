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
    
    def select_by_date(self, date, id_user):
        sql = """SELECT id,id_user,humor,descricao,CAST(created_at as DATE) FROM tbl_desabafo WHERE id_user = %s AND CAST(created_at as TEXT) < %s"""
        print(sql)
        with self.db.read_cursor() as c:
            c.execute(sql, (id_user, date))
            confessions_data = c.fetchall()
            
        confessions_model = ConfessionMapper.to_confession_model_list(confessions_data) 
        return confessions_model
        
    def select_last_thirty_days(self, id_user):
        sql = "SELECT id,id_user,humor,descricao,created_at FROM tbl_desabafo WHERE id_user = %s AND DATE_SUB(NOW(), INTERVAL 30 DAY) ORDER BY created_at ASC"
        with self.db.read_cursor() as c:
            c.execute(sql, (id_user,))
            confessions_data = c.fetchall()

        confessions_model = ConfessionMapper.to_confession_model_list(confessions_data)
        return confessions_model
        