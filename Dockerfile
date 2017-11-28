FROM python:3.6.3
MAINTAINER john s
RUN mkdir -p /var/www/bookmarker
WORKDIR /var/www/bookmarker
ADD requirements.txt /var/www/bookmarker/
RUN pip install -r requirements.txt
ADD . /var/www/bookmarker
