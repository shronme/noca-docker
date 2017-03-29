FROM ubuntu:14.04
MAINTAINER Ron Shteinberg <ron.shteinberg@liberis.co.uk>

ENV DEBIAN_FRONTEND noninteractive
ENV POSTGRES_CONNECTION postgresql://newable:newableadmin@
ENV SQLALCHEMY_DATABASE_URI aa156b48w454tic.ctaks54dcv5t.eu-west-1.rds.amazonaws.com


RUN apt-get update && apt-get install -y \
    python-pip python-dev uwsgi-plugin-python \
    nginx supervisor
RUN apt-get install libffi-dev
RUN apt-get install -y libpq-dev gcc

COPY flask.conf /etc/nginx/sites-available/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY app /var/www/app
RUN mkdir /var/www/alembic
COPY alembic /var/www/alembic
COPY application.py /var/www/app
COPY alembic.ini /var/www/
COPY requirements.txt /var/www
COPY uwsgi.ini /var/www
COPY fe/src/app /var/www


RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor \
    && rm /etc/nginx/sites-enabled/default \
    && ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf \
    && echo "daemon off;" >> /etc/nginx/nginx.conf \
    &&  pip install -r /var/www/requirements.txt \
    && chown -R www-data:www-data /var/www/app \
    && chown -R www-data:www-data /var/log

EXPOSE 80 443

CMD ["/usr/bin/supervisord"]