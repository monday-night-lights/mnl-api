FROM python:3.6-alpine

RUN ifconfig -a || ip a l

COPY requirements.txt /requirements.txt

RUN apk update && apk add bash
RUN set -ex \
  && apk add --no-cache --virtual .build-deps \
    gcc \
    make \
    libc-dev \
    musl-dev \
    linux-headers \
    pcre-dev \
    postgresql-dev \
    postgresql-client \
    python3-dev \
  && python3.6 -m venv /venv \
  && /venv/bin/pip install -U pip \
  && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r /requirements.txt" \
  && runDeps="$( \
    scanelf --needed --nobanner --recursive /venv \
      | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
      | sort -u \
      | xargs -r apk info --installed \
      | sort -u \
  )" \
  && apk add --virtual .python-rundeps $runDeps \
  && apk del .build-deps

WORKDIR /srv/
COPY . .

EXPOSE 8000

ENTRYPOINT ["/srv/init.sh"]
