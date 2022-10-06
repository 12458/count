FROM python:slim


ENV PYTHONUNBUFFERED True
ENV MEMCACHED_ADDR memcached
ENV APP_HOME /code
ENV PORT 5000


WORKDIR $APP_HOME
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code/app
EXPOSE $PORT
CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 app.main:app
