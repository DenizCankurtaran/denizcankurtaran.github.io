# Dockerfile:

FROM python:3.9-buster

WORKDIR /src/app

RUN mkdir data

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY * .

ENV FLASK_APP=main.py

CMD ["flask", "run", "--host", "0.0.0.0"]


# docker-compose.yaml

version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5001:5000"
    volumes:
      - data:/src/app/data
  app1:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5002:5000"
    volumes:
      - data1:/src/app/data

volumes:
  data:
  data1:

# Mariadb:
- docker pull mariadb:10.7 
- docker run -p 3306:3306 --env MARIADB_ROOT_PASSWORD=1234 mariadb:10.7 
- in shell:
  - mysql -u root -p
  - show databases;
  - use mysql;
  - show tables;
  - select User from user;
  - exit;
  - exit

