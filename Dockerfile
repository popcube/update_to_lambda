FROM python:3
USER root

COPY . .
RUN pip install -U --no-index --find-links=./packages pip \
  && pip install --no-index --find-links=./packages -r requirements.txt