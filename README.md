# Тестовое задание.
Программа, принимающая на вход количество параллельных обращений к сервису-клиенту, количество пакетов которые он отправит сервису-обработчику и верхнюю границу диапазона значений в секундах, имитирующих задержку при выполнении обработки запроса. На выход записывает два .txt файла с необходимыми данными.
### Текст тестового здесь приводить не буду, только краткую инструкцию по запуску и работе.
## Подготовка к работе.
### Клонируйте репозиторий:
```
git clone git@github.com:pdyakovlev/data_writing_delay_test_task.git
```
### Соберите и запустите контейнеры:
```
docker compose build
docker compose up
```
## Работа с программой.
### Можно сразу перейти на http://127.0.0.1:8003, ниже чуть подробнее.
### GET запросы.
Программа запускается на localhost, контейнеры работают на портах 8001, 8002, 8003. GET запросы по адресам http://127.0.0.1:8001 (вернёт 'receiver') и http://127.0.0.1:8002 (вернёт 'handler') используются для быстрой проверки, можно выполнять в браузере.
### POST запрос.
Для запуска программы перейдите на страницу клиента программы (http://127.0.0.1:8003), введите свои параметры и нажмите кнопку старт, или выполните POST запрос на http://127.0.0.1:8003/request через Postman, передав при этом в **Body/form-data** ключи **connection_count**, **connection_value**, **delay_range**.
### Результаты выполнения.
Логи, пишушиеся в процессе работы программы, вы можете посмотреть в контейнерах client и receiver, файлы .txt (first.txt, second.txt) вы можете найти в контейнере handler в папке handler.
## Стек.
- [Python](https://www.python.org/);
- [FastAPI](https://fastapi.tiangolo.com/);
- [Asyncio](https://docs.python.org/3/library/asyncio.html);
