from fastapi import APIRouter

from db.mysql import engineconn
from model.workflow_card import WorkFlowCard

cardRouter = APIRouter(
    prefix="/card",
    tags=["card"]
)

engine = engineconn()
session = engine.sessionmaker()

@cardRouter.post("/getCard")
async def get_workflow(flow_id):
    example = session.query(WorkFlowCard).filter(WorkFlowCard.workflow_id==flow_id).all()
    # example = session.query(WorkFlowCard).all()
    return [
        {
            "title": example,
        }
    ]