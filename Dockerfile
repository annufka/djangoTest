# syntax=docker/dockerfile:1
FROM python:3.8.2
ENV PYTHONUNBUFFERED=1
WORKDIR /djangoTest
COPY requirements.txt /djangoTest
RUN pip install -r requirements.txt
COPY . /djangoTest