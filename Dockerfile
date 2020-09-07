FROM python:3.7-slim-buster

RUN apt update && apt install -y git && apt clean

COPY requirements.txt /project/
WORKDIR /project

RUN pip install -r requirements.txt