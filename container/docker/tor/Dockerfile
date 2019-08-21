FROM byeong0/python:3.6


# Install dependencies
RUN apt-get update && \
    apt-get install -y \
    net-tools \
    tor && \
	rm -rf /var/lib/apt/lists/*

#pip install
RUN    pip install --user --upgrade pip==19.2.2 \
    && pip install flask stem fake_useragent PySocks googletrans

COPY test.py /usr/src/app/test.py
COPY run_test_proxies.sh /usr/src/app/run_test_proxies.sh
RUN chmod 750 /usr/src/app/run_test_proxies.sh

WORKDIR /usr/src/app

EXPOSE 80

CMD [ "./run_test_proxies.sh"]

