# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY . /app
