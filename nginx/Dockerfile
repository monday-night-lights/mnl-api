FROM nginx:1.13.6-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/ /etc/nginx/conf.d

COPY ssl/ /etc/ssl/
