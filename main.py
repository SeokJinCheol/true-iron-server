from fastapi import FastAPI

from api.router import apiRouter

app = FastAPI()

app.include_router(apiRouter)
