import asyncio
import random
import time

import aiohttp
from fastapi import FastAPI, Request

app = FastAPI()


async def make_requests(t_id: int, get_id, d_r: int, val_by_cnt: int):
    """Функция, которая посылает необходимое число запросов."""
    async with aiohttp.ClientSession() as session:
        for i in range(val_by_cnt):
            id = get_id.__next__()
            delay = random.randint(1, d_r)
            data = {'id': id,
                    'delay': delay}
            time_now = time.strftime('%H:%M:%S')
            await session.post('http://receiver:8001/receive',
                               data=data)
            log_msg = (f'Время запроса {time_now}, номер потока {t_id},'
                       f' номер запроса {i}, запрос: id: {id}; delay: {delay}')
            print(log_msg)


@app.get('/')
async def get_client():
    return 'client'


@app.post('/request')
async def client(request: Request):
    """Стартовая функция сервиса, подготавливает данные и вызывает tasks()."""
    connection_count = request.headers.get('connection_count')
    connection_value = request.headers.get('connection_value')
    delay_range = request.headers.get('delay_range')
    try:
        d_r = int(delay_range)
        c_cnt = int(connection_count)
        c_val = int(connection_value)
        val_by_cnt = int(c_val / c_cnt)
        get_id = id_generator(c_val)
        return await tasks(c_cnt, get_id, d_r, val_by_cnt)
    except Exception:
        return 'Возникло исключение, проверьте введённые данные.'


async def tasks(c_cnt, get_id, d_r, val_by_cnt):
    """Функция стартующая asyncio."""
    tasks = [make_requests(i, get_id, d_r, val_by_cnt) for i in range(c_cnt)]
    await asyncio.gather(*tasks)
    return "Complete!"


def id_generator(c_val: int):
    """Простой генератор id."""
    num = 0
    while num < c_val:
        yield num
        num += 1
