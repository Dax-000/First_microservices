from fastapi import FastAPI, APIRouter
import uvicorn

from database import add as log_entry
from database import get_all as get_history


app = FastAPI()
router = APIRouter()


@router.get('/greet')
def greet(name: str = None):
    log_entry(name)
    return f"Привет, {name} от Python!"


@router.get('/greet/history')
def history():
    return get_history()


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True, workers=1)