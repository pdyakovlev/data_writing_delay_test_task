import asyncio
import random
import time

import aiohttp
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


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


@app.get("/", response_class=HTMLResponse)
async def client_get(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.post('/request')
async def client(connection_count: int = Form(...),
                 connection_value: int = Form(...),
                 delay_range: int = Form(...)):
    """Стартовая функция сервиса, подготавливает данные и вызывает tasks()."""
    try:
        val_by_cnt = int(connection_value / connection_count)
        get_id = id_generator(connection_value)
        return await tasks(connection_count, get_id, delay_range, val_by_cnt)
    except Exception:
        return 'Возникло исключение, проверьте введённые данные.'


async def tasks(c_cnt: int,
                get_id,
                d_r: int,
                val_by_cnt: int):
    """Функция стартующая asyncio."""
    tasks = [make_requests(i, get_id, d_r, val_by_cnt) for i in range(c_cnt)]
    await asyncio.gather(*tasks)
    return 'Complete!'


def id_generator(c_val: int):
    """Простой генератор id."""
    num = 0
    while num < c_val:
        yield num
        num += 1
