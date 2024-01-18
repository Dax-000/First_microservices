from fastapi import FastAPI, APIRouter
import uvicorn

from database import add as log_entry
from database import get_all as get_history
from config import app_host, app_port, app_workers


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
    uvicorn.run('main:app', host=app_host, port=app_port, reload=True, workers=app_workers)
