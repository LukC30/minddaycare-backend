from sqlite3 import DatabaseError
from contextlib import contextmanager
import logging
import mysql.connector

logger = logging.getLogger("[DATABASE]")

class Database():
    def __init__(self):
        self.db = self.connection()
    
    def connection(self):
        try:
            db = mysql.connector.connect(
                user="root",
                password="",
                port=3306,
                host="localhost",
                database="DB_MINDDAYCARE"
            )
            
            logger.info("Database is initialized")
            return db
        except DatabaseError as e:
            logger.error(f"Connection error {e}")

    @contextmanager
    def alter_cursor(self):
        c = self.db.cursor()
        try:
            yield c
            self.db.commit()
        except DatabaseError as e:
            self.db.rollback()
            logger.error(f"Write transaction failed: {e}")
            raise
        finally:
            c.close()
    
    @contextmanager
    def read_cursor(self):
        c = self.db.cursor()
        try:
            yield c
        except DatabaseError as e:
            logger.error("The read transaction is failed: %s", str(e))
            raise
        finally:
            c.close()

    
