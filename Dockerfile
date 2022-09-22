# Dockerfile

FROM python:3.9-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/faq
COPY requirements/base.txt requirements/prod.txt start.sh /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY src /opt/app/faq/
WORKDIR /opt/app
RUN pip install -r prod.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
ENTRYPOINT [ "/opt/app/start.sh" ]
