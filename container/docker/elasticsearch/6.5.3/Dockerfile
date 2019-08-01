FROM docker.elastic.co/elasticsearch/elasticsearch:6.5.3

MAINTAINER Byeong0, <byeong0@gmail.com>

RUN bin/elasticsearch-plugin install analysis-nori

COPY --chown=elasticsearch:elasticsearch elasticsearch.yml /usr/share/elasticsearch/config/
COPY --chown=elasticsearch:elasticsearch jvm.options /usr/share/elasticsearch/config/

COPY limits.conf /etc/security/

#EXPOSE 9200
#EXPOSE 9300

#HEALTHCHECK --interval=15s --timeout=15s CMD wget -qO- http://127.0.0.19200/_cat/health
