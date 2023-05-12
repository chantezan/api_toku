FROM python:3.9-buster
RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev \
    librtmp-dev \
    openssl \
    libssl-dev
ENV PYTHONUNBUFFERED 1

RUN mkdir /code;
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install uwsgi
RUN mkdir /temp ;
EXPOSE 8005 2222