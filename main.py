from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.router import apiRouter

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(apiRouter)
