FROM python:3.9

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
# $PORT is set by heroku
ENV PORT=8888

# Install system dependencies with OpenCV
RUN apt-get update
RUN apt-get install -y gcc python3-dev musl-dev libpq-dev

RUN mkdir /code
WORKDIR /code
COPY requirements/dev.requirements.txt /code/
RUN pip install -r  /code/dev.requirements.txt
COPY . /code/

COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

CMD ["docker-entrypoint.sh"]
