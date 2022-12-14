from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return { 'data': 'home page'}

@app.get('/api/home')
def homePage():
    return { 'data': 'api home page'}