from fastapi import APIRouter
from api.workflow.card.router import cardRouter

from db.mysql import engineconn
from model.workflow import Workflow
from util.redis import redis_config

workflowRouter = APIRouter(
    prefix="/workflow",
    tags=["workflow"]
)

workflowRouter.include_router(cardRouter)

engine = engineconn()
session = engine.sessionmaker()

@workflowRouter.get("/getWorkflowList")
async def get_workflow():
    example = session.query(Workflow).all()
    return [
        {
            "title": example,
        }
    ]



@workflowRouter.get("/getRedisSample")
async def get_workflow():
    rd = redis_config()
    print(rd)
    return [
        {
            "title": rd.get('juice'),
        }
    ]

@workflowRouter.post("/postRedisSample")
async def get_workflow(id):
    rd = redis_config()
    rd.set("juice", id)  # set
    return {
        "data": rd.get("juice")  # get
    }