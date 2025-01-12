FROM python:3.10-alpine3.21

LABEL maintainer="szymon-wais.netlify.app"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app


WORKDIR /app
EXPOSE 8000

# Install required dependencies for GDAL
RUN apk update && apk add --no-cache \
    gdal-dev \
    geos-dev \
    proj-dev \
    musl-dev \
    gcc \
    g++

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app

# Clean up build dependencies (optional)
RUN apk del gcc g++

ENV PATH="/py/bin:$PATH"

USER app

# CMD ["run.sh"]


