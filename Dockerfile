FROM python:3.8-alpine as api
RUN adduser -s /bin/sh -D -u 1000 flat flat
RUN apk update && apk add bash
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk upgrade && apk add --no-cache --virtual build-dependencies linux-headers postgresql-client \
postgresql-dev linux-headers make gcc g++ libffi-dev libxml2-dev libxslt-dev libldap \
libsasl jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev \
tk-dev tcl-dev && rm -rf /var/cache/apk/*

WORKDIR /home/api/
COPY api/requirements ./requirements
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

FROM api as dev
WORKDIR /home/api/
USER root
COPY --chown=flat:flat ./api ./api
USER flat
RUN pip install -r requirements/local.txt


