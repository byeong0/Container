# github
https://github.com/byeong0/routine

# docker build path
container/docker/faiss

# docker build name
- byeong0/faiss-cpu:latest
- byeong0/faiss-gpu:9.0-cudnn7
- byeong0/faiss-gpu:10.0-cudnn7
<pre>
sudo docker build --tag byeong0/faiss-cpu:latest -f cpu/Dockerfile .
sudo docker build --tag byeong0/faiss-gpu:9.0-cudnn7 -f gpu/9.0-cudnn7/Dockerfile .
sudo docker build --tag byeong0/faiss-gpu:10.0-cudnn7 -f gpu/10.0-cudnn7/Dockerfile .
</pre>
