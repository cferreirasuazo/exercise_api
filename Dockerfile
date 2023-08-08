# syntax=docker/dockerfile:1
FROM python:3.12.0b4-bookworm
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt-get update -y && apt-get install apt-utils wait-for-it -y --no-install-recommends
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
