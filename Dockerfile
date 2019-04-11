FROM nimmis/apache-php7
MAINTAINER Zedd <zeddyu.lu@gmail.com>

# COPY ./sources.list /etc/apt/sources.list
RUN apt-get update && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/www/html/*

RUN mkdir -p /etc/service/apache2/ && \
    printf "#!/bin/sh\n\nexec /usr/sbin/apachectl -D FOREGROUND\n" > /etc/service/apache2/run

COPY ./php.ini /etc/php/7.0/cli

ADD ./html /var/www/html
RUN echo "flag{This_is_fl4g}" >> /flag

EXPOSE 80