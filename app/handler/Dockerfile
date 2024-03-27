FROM python:latest
WORKDIR /handler
COPY requirements.txt /handler/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /handler/requirements.txt
COPY handler.py /handler/handler.py
COPY writer.py /handler/writer.py
CMD ["uvicorn", "handler:app", "--host", "0.0.0.0", "--port", "8002"]