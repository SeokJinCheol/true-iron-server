from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker

from db.mysql import engineconn
from model.workflow import Workflow

workflowRouter = APIRouter(
    prefix="/workflow",
    tags=["workflow"]
)

engine = engineconn()
session = engine.sessionmaker()

@workflowRouter.post("/getWorkflowList")
async def get_workflow():
    example = session.query(Workflow).all()
    return [
        {
            "title": example,
        }
    ]



@workflowRouter.post("/getWorkflowList2")
async def get_workflow():
    return [
        {
            "title": "test",
        }
    ]