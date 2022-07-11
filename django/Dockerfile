FROM python:3.8

RUN apt-get update
RUN apt-get install -y \
  netcat \
;

RUN pip install pipenv
ENV PATH $PATH:/root/.local/bin
ENV PIP_NO_BINARY psycopg2

WORKDIR /srv/mnl
COPY Pipfile .
COPY Pipfile.lock .
RUN set -ex && pipenv lock && pipenv install --deploy --system

COPY . .
ENTRYPOINT ["./entrypoint.sh"]
