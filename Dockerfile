FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN export FLASK_ENV=development

COPY ./app /app
