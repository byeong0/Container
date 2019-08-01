# github
https://github.com/byeong0/routine

# docker build path
container/docker/anaconda3/

# docker build name
byeong0/anaconda3:9.0-cudnn7
byeong0/anaconda3:10.0-cudnn7
byeong0/anaconda3:cpu
<pre>
sudo docker build --tag byeong0/anaconda3:9.0-cudnn7 -f 9.0-cudnn7/Dockerfile .
sudo docker build --tag byeong0/anaconda3:10.0-cudnn7 -f 10.0-cudnn7/Dockerfile .
sudo docker build --tag byeong0/anaconda3:cpu -f cpu/Dockerfile .
</pre>
