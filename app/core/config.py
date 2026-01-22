import logging
import os
from dotenv import load_dotenv

def get_database_env():
    envs = {
            "DATABASE_HOST": "",
             "DATABASE_PORT":0,
             "DATABASE_PASSWORD" : "",
             "DATABASE_USER" : ""
        }
    
    for k in envs.keys():
        envs[k] = os.getenv(k, "")
        
    return envs

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )