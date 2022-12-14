from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return { 'data': 'working with multiple branches again 2-1'}