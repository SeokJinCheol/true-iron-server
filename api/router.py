from fastapi import APIRouter

from api.auth.router import authRouter
from api.workflow.router import workflowRouter

apiRouter = APIRouter(
    prefix="/api"
)

apiRouter.include_router(workflowRouter)
apiRouter.include_router(authRouter)