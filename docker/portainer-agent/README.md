# docker build path
ssg-brain-app/

# docker build name
- ssgbrain.azurecr.io/ssg-brain-portainer:latest
<pre>
sudo docker build --tag ssgbrain.azurecr.io/ssg-brain-portainer-agent:latest -f ssg-brain-app/container/common/docker/portainer-agent/Dockerfile .
</pre>