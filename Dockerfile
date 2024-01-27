FROM python:3
USER root

COPY ./packages ./packages
COPY Dockerfile main.py requirements.txt .
RUN pip install -U --no-index --find-links=./packages pip \
  && pip install --no-index --find-links=./packages -r requirements.txt