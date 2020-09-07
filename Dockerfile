FROM python:3.7-slim-buster

RUN apt update && apt install -y git && apt clean