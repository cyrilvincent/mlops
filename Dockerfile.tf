# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements-tf.txt,target=requirements-tf.txt \
    python -m pip install -r requirements-tf.txt
RUN mkdir -p temp

COPY data/cancer/*.h5 data/cancer/
COPY data/cancer/*.p*kl* data/cancer/
COPY data/dogsvscats/*.h5 data/dogsvscats/
COPY data/mnist/*.h5 data/mnist/
COPY api_tf.py .
COPY config.py .
COPY tensorflow_service.py .
EXPOSE 5001
CMD python api_tf.py

# docker build -t api-tf -f Dockerfile.tf .
# docker run -p 5001:5001 api-tf
# docker-compose up --build

