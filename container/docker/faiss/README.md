# github
https://github.com/byeong0/routine

# docker build path
container/docker/faiss

# docker build name
- byeong0/faiss:cpu
- byeong0/faiss:9.0-cudnn7
- byeong0/faiss:10.0-cudnn7
<pre>
sudo docker build --tag byeong0/faiss:cpu -f cpu/Dockerfile .
sudo docker build --tag byeong0/faiss:9.0-cudnn7 -f 9.0-cudnn7/Dockerfile .
sudo docker build --tag byeong0/faiss:10.0-cudnn7 -f 10.0-cudnn7/Dockerfile .
</pre>
