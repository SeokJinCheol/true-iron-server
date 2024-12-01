from fastapi import APIRouter
from api.workflow.card.router import cardRouter

from db.mysql import engineconn
from model.workflow import Workflow

workflowRouter = APIRouter(
    prefix="/workflow",
    tags=["workflow"]
)

workflowRouter.include_router(cardRouter)

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