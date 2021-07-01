FROM python:3.8-alpine as api
RUN apk update && apk add bash
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk upgrade && apk add --no-cache --virtual build-dependencies linux-headers postgresql-client \
postgresql-dev linux-headers make gcc g++ libffi-dev libxml2-dev libxslt-dev libldap \
libsasl jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev \
tk-dev tcl-dev && rm -rf /var/cache/apk/*

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1


# create root directory for our project in the container
RUN mkdir /git_api

# Set the working directory to /api
WORKDIR /git_api

# Copy the current directory contents into the container at /api
ADD ./api /git_api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements/local.txt

