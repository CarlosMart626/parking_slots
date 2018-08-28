FROM python:3.6

ENV CODE=/code

COPY requirements.txt /
RUN pip install -r requirements.txt

WORKDIR $CODE
VOLUME $CODE
