import time

from fastapi import FastAPI, Form
from writer import Writer

app = FastAPI()


@app.get('/')
async def handler():
    return 'hander'


@app.post('/handle')
async def handle(id: int = Form(...), delay: int = Form(...)) -> None:
    """Сервис-обработчик запросов который ставит задачу на паузу
    на N секунд исходя из параметра запроса"""
    recieve_time = time.strftime('%H:%M:%S')
    wr = Writer()
    wr.write(2, 'second', id)
    time.sleep(delay)
    wr.write(1, 'first', id, recieve_time=recieve_time)
