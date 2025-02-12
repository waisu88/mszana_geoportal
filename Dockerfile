FROM python:3.10-alpine3.21

LABEL maintainer="szymon-wais.netlify.app"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

# Install required dependencies for GDAL
RUN apk update && apk add --no-cache \
    gdal \
    gdal-dev \
    gdal-tools \
    geos-dev \
    proj-dev \
    # musl-dev \
    gcc \
    g++ \
    libstdc++ \
    postgresql-client \
    curl && \
    ln -s /usr/lib/libgdal.so /usr/lib/libgdal.so.3

# Create Python virtual environment and install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev  linux-headers && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

RUN /py/bin/pip install --no-cache-dir "GDAL==$(gdal-config --version)"
# RUN /py/bin/pip install --no-cache-dir --no-binary GDAL GDAL

# Set environment variables for GDAL and GEOS
# ENV GDAL_LIBRARY_PATH=/usr/lib/libgdal.so
# ENV GEOS_LIBRARY_PATH=/usr/lib/libgeos_c.so

# Clean up build dependencies (optional)
RUN apk del gcc g++

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]
