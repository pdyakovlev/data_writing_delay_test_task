# Тестовое задание.
Программа, принимающая на вход количество параллельных обращений к сервису-клиенту, количество пакетов которые он отправит сервису-обработчику и верхнюю границу диапазона значений в секундах, имитирующих задержку при выполнении обработки запроса. На выход записывает два .txt файла с необходимыми данными.
### Текст тестового здесь приводить не буду, только краткую инструкцию по запуску и работе.
## Подготовка к работе.
### Клонируйте репозиторий:
```
git clone git@github.com:pdyakovlev/data_writing_delay_test_task.git
```
### Создайте виртуальное окружение в корне:
```
python -m venv venv
```
### Активируйте виртуальное окружение:
```
. venv/Scripts/activate
```
### Установите зависимости:
```
pip install -r requirements.txt
```
### Соберите и запустите контейнеры:
```
docker compose build
docker compose up
```
## Работа с программой.
### GET запросы.
Программа запускается на localhost, контейнеры работают на портах 8001, 8002, 8003. GET запросы по адресам http://127.0.0.1:8001 (вернёт 'receiver'), http://127.0.0.1:8002 (вернёт 'handler') и http://127.0.0.1:8003 (вернёт 'client') используются для быстрой проверки, можно выполнять в браузере.
### POST запрос.
Для запуска программы выполните POST запрос на http://127.0.0.1:8003/request через Postman, передав при этом в **Headers** ключи **connection_count**, **connection_value**, **delay_range**.
### Результаты выполнения.
Логи, пишушиеся в процессе работы программы, вы можете посмотреть в контейнерах client и receiver, файлы .txt (first.txt, second.txt) вы можете найти в контейнере handler в папке handler.
