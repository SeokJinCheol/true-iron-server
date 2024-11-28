from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('mysql.host')
port = os.getenv('mysql.port')
user = os.getenv('mysql.user')
password = os.getenv('mysql.password')
database = os.getenv('mysql.database')

DB_URL = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'

print(DB_URL)

engine = create_engine(DB_URL)

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

    def connection(self):
        conn = self.engine.connect()
        return conn