FROM python:3.11-slim-bullseye

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV PIP_ROOT_USER_ACTION=ignore


RUN apt-get update \
    && apt-get -y install build-essential \
    && apt-get -y install libpq-dev gcc \
    && apt-get -y install netcat \
    && apt-get -y install curl

RUN curl -fsSL -o /usr/local/bin/dbmate https://github.com/amacneil/dbmate/releases/latest/download/dbmate-linux-amd64 \
&& chmod +x /usr/local/bin/dbmate


COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "./scripts/run.sh"]