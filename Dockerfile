FROM python:2
MAINTAINER john s
RUN mkdir -p /var/www/bookmarker
WORKDIR /var/www/bookmarker
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /var/www/bookmarker
WORKDIR /var/www/bookmarker
RUN pip install -r requirements.txt
ADD . /var/www/bookmarker
