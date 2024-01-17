from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/greet')
def greet(name: str = None):
    return f"Привет, {name} от Python!"


if __name__ == "__main__":
    uvicorn.run('main:app', reload=True, workers=1)