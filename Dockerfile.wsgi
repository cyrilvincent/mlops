# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

RUN apt-get -y update
RUN apt-get -y install gcc
RUN python -m pip install uWSGI==2.0.23
COPY nginx/uwsgi.ini .

COPY data/cancer/*.pickle data/cancer/
COPY data/house/*.pickle data/house/
COPY data/mnist/*.pickle data/mnist/
COPY api.py .
COPY sklearn_service.py .
COPY logging.ini .

EXPOSE 9090

CMD uwsgi --ini uwsgi.ini
