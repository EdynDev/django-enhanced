FROM python:3.8.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install deb packages
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends \
    vim \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /home/server

COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

# RUN pip install --upgrade pip && pip install pipenv && pipenv install --system --deploy


ENTRYPOINT [ "./docker-entrypoint.sh" ]

# EXPOSE 8001
