FROM lgatica/redis-sentinel:4.0.2

## Copy Redis File
## 복사/추가 하는파일의 Container내 경로는 항상 절대경로로 작성하여야 한다.
RUN rm -rf /usr/local/bin/sentinel-entrypoint.sh
#COPY docker/container/redis/sentinel/sentinel.conf /usr/local/bin/sentinel.conf
COPY container/docker/redis/sentinel/sentinel-entrypoint.sh /usr/local/bin/sentinel-entrypoint.sh

## change access authority
#RUN chmod 755 /usr/local/bin/sentinel.conf
RUN chmod 755 /usr/local/bin/sentinel-entrypoint.sh
#RUN chown redis:redis /usr/local/bin/sentinel.conf
RUN chown redis:redis /usr/local/bin/sentinel-entrypoint.sh

EXPOSE $CLIENTPORT
ENTRYPOINT ["/usr/local/bin/sentinel-entrypoint.sh"]
CMD [ "redis-server","/usr/local/bin/conf/sentinel.conf", "--sentinel" ]