# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

RUN apt-get -y update
RUN apt-get -y install gcc
# RUN python -m pip install uWSGI==2.0.23
RUN python -m pip install uvicorn[standard]
COPY nginx/uwsgi.ini .

COPY data/cancer/*.p*kl* data/cancer/
COPY data/house/*.* data/house/
COPY data/mnist/*.p*kl* data/mnist/
COPY api.py .
COPY config.py .
COPY sklearn_service.py .

EXPOSE 9090

# CMD uwsgi --ini uwsgi.ini  # Flask only

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "9090", "--workers", "4"]

