from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return "Hello World"
    
@app.get("/heartbeat")
def hertbeat():
    return "heartbeat"