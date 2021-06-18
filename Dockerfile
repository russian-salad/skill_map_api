FROM python:3.8-slim

WORKDIR /app

COPY requirements.dev.txt requirements.dev.txt

RUN pip install -r requirements.dev.txt

COPY . . 

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
