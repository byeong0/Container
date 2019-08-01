FROM byeong0/anaconda3:10.0-cudnn7
#https://hub.docker.com/r/continuumio/anaconda3/

MAINTAINER Byeong0, <byeong0@gmail.com>

# Install dependencies and create dirs
RUN apt-get -qq update && apt-get install -y software-properties-common apt-utils locales tzdata \
        libssl-dev \
		libmysqlclient-dev \
		python-opencv \
        curl \
        vim \
        git \
        wget \
        locales \
    && rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL C.UTF-8

COPY requirements.txt /usr/src/
WORKDIR /usr/src/

#pip install
RUN    pip install --user --upgrade pip==18.1 \
    && pip install -r /usr/src/requirements.txt

RUN conda install -y faiss-gpu cudatoolkit=10.0 -c pytorch # For CUDA9