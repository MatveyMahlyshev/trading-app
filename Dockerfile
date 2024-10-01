FROM python:3.12-alpine3.20

WORKDIR /trading

EXPOSE 8000

COPY requirements.txt /trading/requirements.txt

COPY trading /trading

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install --no-cache-dir -r /trading/requirements.txt

RUN adduser --disabled-password trading-user

USER trading-user