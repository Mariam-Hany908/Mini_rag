from fastapi import FastAPI

app = FastAPI()


@app.get("/welcome")
def welcome():
    message = "Welcome to mini-RAG app"
    return {"message": message}