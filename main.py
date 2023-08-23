import uvicorn
from fastapi import FastAPI

from routers import user

app = FastAPI()
app.include_router(user.router, prefix = '/user')


@app.get('/')
async def index():
    return {'message': 'Hello, how are u?'}


if __name__ == '__main__':
    uvicorn.run('main:app', host = '127.0.0.1', port = 8080, workers = 4, reload = True)
