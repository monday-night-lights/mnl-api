FROM nginx:stable-alpine

# Create development SSL key and certificate
RUN set -ex && apk add --no-cache openssl
COPY ssl/ /etc/ssl
RUN openssl req -x509 -nodes -days 365 -newkey rsa -config /etc/ssl/dev.conf \
                                                   -keyout /etc/ssl/dev.key \
                                                   -out /etc/ssl/dev.crt

RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/ /etc/nginx/conf.d
