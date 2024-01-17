from fastapi import FastAPI
import uvicorn

from database import add as log_entry


app = FastAPI()


@app.get('/greet')
def greet(name: str = None):
    log_entry(name)
    return f"Привет, {name} от Python!"


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True, workers=1)