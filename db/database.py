from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

class enginconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle= 500)

        def sessionmaker(self):
            Session = sessionmaker(bind=self.engin)
            session = Session()
            return session

        def connect(self):
            conn = self.engine.connect()
            return conn