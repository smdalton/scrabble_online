FROM ubuntu:16.04

MAINTAINER Shane Dalton "shanemdalton@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]

COPY . /usr/src/app
CMD [ "app.py" ]