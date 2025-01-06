from fastapi import APIRouter
from api.workflow.card.router import cardRouter

from db.mysql import engineconn
from model.workflow import Workflow

workflowRouter = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

