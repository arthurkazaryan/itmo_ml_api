FROM python:3.10

ENV TZ="Europe/Paris"
ENV PYTHONUNBUFFERED 1
COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get install libsm6 libxext6 gcc git -y
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
