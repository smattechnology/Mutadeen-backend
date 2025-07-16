from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.post import router as postRouter

app = FastAPI(
    title="Mutadeen Admin",
    version="0.1.1",
    description="Mutadeen backend api"
)

# Allow requests from your frontend
origins = [
    "http://localhost:3000",  # React dev server
    # Add production domain when deploying
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # Or use ["*"] for all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(postRouter)