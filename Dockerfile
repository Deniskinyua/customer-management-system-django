FROM python:3.12-slim-bullseye
ENV PYTHONUNBUIFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /app
COPY . /app/
RUN apt-get update
COPY ./requirements.txt .
RUN pip install -r requirements.txt
