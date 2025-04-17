from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"mensagem": "Olá, Docker com FastAPI!"}