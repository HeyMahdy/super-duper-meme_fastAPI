from fastapi import FastAPI
from api.h import router as h_router
app = FastAPI()

app.include_router(h_router)
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
