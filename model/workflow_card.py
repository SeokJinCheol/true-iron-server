from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class WorkFlowCard(Base):
    __tablename__ = 'workflow_card'

    id = Column(Integer, autoincrement=True, primary_key=True)
    workflow_id = Column(Integer, ForeignKey('workflow.id'))
    target_card_id = Column(Integer)
    title = Column(String)
    location_x = Column(Integer)
    location_y = Column(Integer)
    create_dt = Column(DateTime)
    update_dt = Column(DateTime)
    dueDate_dt = Column(DateTime)