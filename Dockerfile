
FROM python:3.7-slim-buster

RUN apt-get -y update
RUN apt-get -y upgrade

COPY shop /opt/api
COPY requirements.txt /opt/api/requirements.txt

WORKDIR /opt/api/
RUN pip install -r requirements.txt

WORKDIR /opt/api/
