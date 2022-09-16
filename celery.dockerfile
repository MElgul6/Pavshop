FROM python:3.10

RUN apt-get upgrade & apt update

WORKDIR /code
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
