# docker build path
ssg-brain-app/


# docker build name
- ssgbrain.azurecr.io/ssg-brain-redis:5.0.4
<pre>
sudo docker build --tag ssgbrain.azurecr.io/ssg-brain-redis:5.0.4 -f ssg-brain-app/container/common/docker/redis/5.0.4/Dockerfile .
</pre>


#참고
https://github.com/bitnami/bitnami-docker-redis