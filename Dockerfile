FROM python:3.10-slim-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
ENV PROJECT_DIR=/opt/app
# copy source and install dependencies
RUN mkdir -p $PROJECT_DIR
RUN mkdir -p $PROJECT_DIR/pip_cache
RUN mkdir -p $PROJECT_DIR
COPY requirements/base.txt requirements/prod.txt start.sh $PROJECT_DIR
COPY src $PROJECT_DIR
WORKDIR $PROJECT_DIR
RUN pip install --upgrade pip
RUN pip install -r prod.txt --cache-dir $PROJECT_DIR/pip_cache
RUN chown -R www-data:www-data $PROJECT_DIR

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
ENTRYPOINT [ "/opt/app/start.sh" ]
