FROM python:3.7.2-alpine
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add bash
RUN set -ex \
  && apk add --no-cache \
    gcc \
    make \
    libc-dev \
    musl-dev \
    linux-headers \
    pcre-dev \
    postgresql-dev \
    postgresql-client \
    python3-dev \
;

WORKDIR /srv/mnl
COPY Pipfile .
COPY Pipfile.lock .

RUN pip install pipenv
ENV PATH $PATH:/root/.local/bin
ENV PIP_NO_BINARY psycopg2
RUN set -ex && pipenv install --deploy --system

COPY . .
ENTRYPOINT ["./entrypoint.sh"]
