from fastapi import FastAPI
import uvicorn

app = FastAPI()
 
def start():
    uvicorn.run(app="linkshortener.main:app", reload=True)