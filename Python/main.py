from fastapi import FastAPI, APIRouter
import uvicorn
import psycopg2

from database import add as log_entry
from database import get_all as get_history
from config import app_workers


app = FastAPI()
router = APIRouter()


@router.get('/greet')
async def greet(name: str = None):
    log_entry(name)
    return f"Привет, {name} от Python!"


@router.get('/greet/history')
async def history():
    return get_history()


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=80, reload=True, workers=app_workers)
