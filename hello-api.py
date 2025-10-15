from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return{'message':'Hello World'}


@app.get('/1')
async def root():
    return{'message':'Hello 1 World'}

