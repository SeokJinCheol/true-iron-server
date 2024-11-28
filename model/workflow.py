from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Workflow(Base):
    __tablename__ = 'workflow'

    id = Column(Integer,autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    title = Column(String)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)