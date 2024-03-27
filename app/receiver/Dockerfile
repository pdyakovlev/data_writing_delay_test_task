FROM python:latest
WORKDIR /receiver
COPY requirements.txt /receiver/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /receiver/requirements.txt
COPY receiver.py /receiver/receiver.py
CMD ["uvicorn", "receiver:app", "--host", "0.0.0.0", "--port", "8001"]