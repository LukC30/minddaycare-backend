from sqlite3 import DatabaseError
from contextlib import contextmanager
from typing import TypeVar
import logging
import sqlite3

logger = logging.getLogger("[DATABASE]")

class Database():
    def __init__(self):
        try:
            self.db = sqlite3.connect('database.db')
            logger.info("Database is initialized")
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

    
