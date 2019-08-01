# github
https://github.com/byeong0/routine

# docker build path
container/docker/redis


# docker build name
- byeong0/redis:5.0.4
- byeong0/redis-sentinel:5.0.4
<pre>
sudo docker build --tag byeong0/redis:5.0.4 -f 5.0.4/Dockerfile .
sudo docker build --tag byeong0/redis-sentinel:5.0.4 -f 5.0.4/sentinel/Dockerfile .
</pre>


#참고
https://github.com/bitnami/bitnami-docker-redis