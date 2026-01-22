from sqlite3 import DatabaseError
from contextlib import contextmanager
from ..config import get_database_env
import logging
import mysql.connector
import os

logger = logging.getLogger("[DATABASE]")

class Database():
    def __init__(self):
        self.envs = get_database_env()
        self.db = None
    
    def connection(self, params: dict):
        try:
            self.db = mysql.connector.connect(
                user=params.get('DATABASE_USER'),
                password=params.get('DATABASE_SECRET'),
                port=int(params.get('DATABASE_PORT')),
                host=params.get('DATABASE_HOST'),
                database="DB_MINDDAYCARE"
            )
            
            logger.info("Database is initialized")
        except DatabaseError as e:
            logger.error(f"Connection error {e}")

    def disconnect(self):
        if self.db:
            self.db.close()
            logger.info("Database connection closed")

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

    
