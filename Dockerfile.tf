# syntax=docker/dockerfile:1

FROM tensorflow/tensorflow:2.10.1 as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt
RUN mkdir -p temp

COPY data/cancer/*.h5 data/cancer/
COPY data/cancer/*.pickle data/cancer/
COPY data/dogsvscats/*.h5 data/dogsvscats/
COPY data/mnist/*.h5 data/mnist/
COPY data/mnist/gan/*.h5 data/mnist/gan/
COPY data/drivers/*.h5 data/drivers/
COPY api_tf.py .
COPY tensorflow_service.py .
COPY numpy_serializer.py .
EXPOSE 5001
CMD python api_tf.py
