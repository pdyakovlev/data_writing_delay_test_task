FROM python:latest
WORKDIR /client
COPY requirements.txt /client/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /client/requirements.txt
COPY client.py /client/client.py
CMD ["uvicorn", "client:app", "--host", "0.0.0.0", "--port", "8003"]