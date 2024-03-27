import time

import aiohttp
from fastapi import FastAPI, Form

app = FastAPI()


@app.get('/')
async def receiver():
    return 'receiver'


@app.post('/receive')
async def receive(id: int = Form(...), delay: int = Form(...)):
    """Асинхронный сервис-приемщик получающий запрос и фиксирующий
        время получения запроса"""
    data = {'id': id,
            'delay': delay}
    time_now = time.strftime('%H:%M:%S')
    log_msg = f"Время получения запроса {time_now}"
    print(log_msg)
    async with aiohttp.ClientSession() as session:
        await session.post('http://handler:8002/handle', data=data)
    return {'asyncAnswer': 'Ok'}
