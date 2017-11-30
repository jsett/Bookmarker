FROM python:3.6.3
MAINTAINER john s
RUN mkdir -p /var/www/bookmarker
WORKDIR /var/www/bookmarker
ADD requirements.txt /var/www/bookmarker/
RUN pip install -r requirements.txt
ADD . /var/www/bookmarker
RUN mkdir /phantomjs/
Run wget -O /phantomjs/phantomjs.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
Run tar xvfj /phantomjs/phantomjs.tar.bz2 -C /phantomjs/
RUN rm -f /phantomjs/phantomjs.tar.bz2
RUN mv /phantomjs/phantomjs-* /phantomjs/phantomjs
