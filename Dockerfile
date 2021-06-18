FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.dev.txt 

WORKDIR /app/app

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
