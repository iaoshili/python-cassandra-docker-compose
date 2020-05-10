# pull official base image
FROM python:3.8.1-alpine

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1  # Prevents Python from writing pyc files to disc
ENV PYTHONUNBUFFERED 1  #  stdout and stderr will be sent to terminal in real time

# set working directory
WORKDIR /app

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements-dev.txt /app/requirements-dev.txt
RUN pip install -r requirements-dev.txt

# add app
COPY . /app
