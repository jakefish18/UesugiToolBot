"""
Including every router from /endpoints.
app: FastAPI - main variable for backend launching.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis.asyncio import Redis

from .endpoints import auth, learning_collection, user

api = FastAPI()


@api.on_event("startup")
async def startup():
    redis = Redis(host="localhost", port=6379, db=0)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


origins = [
    "http://localhost:3000",  # Vite (Vue 3) default dev server
    "http://127.0.0.1:3000",  
    "http://127.0.0.1:8000",
    "http://localhost:8000"
]

# Add CORS middleware
api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           
    allow_credentials=True,          
    allow_methods=["GET", "POST", "PUT", "DELETE"],   
    allow_headers=["*"],             
)

api.include_router(auth.router, prefix="/auth", tags=["auth"])
api.include_router(learning_collection.router, prefix="/learning_collections", tags=["learning_collection"])
api.include_router(user.router, prefix="/users", tags=["user"])

