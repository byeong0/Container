# -*- coding:utf-8 -*-
from stem import Signal
from stem.control import Controller
import time
import requests
from fake_useragent import UserAgent
import random, time
import logging
from logging import handlers
from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

# signal TOR for a new connection
def renew_connection():
    renew_connection_strt_time = time.time()
    print('renew_connection begin')
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=HashedControlPassword)
        controller.signal(Signal.NEWNYM)
    print('renew_connection end : {}'.format(time.time() - renew_connection_strt_time))

@app.route("/request", methods=['POST'])
def request_main():
    headers = request.headers
    data = request.json
    print(type(data))
    return send_test_proxies(data.get('text'))

def send_test_proxies(target_text: str) -> str:

    strt_time = time.time()

    if random.randrange(1,10) == 1 :
        renew_connection()

    headers = dict()
    result = None

    try:

        headers = dict()
        headers['Content-Type'] = 'application/json;charset=utf-8'
        headers['User-Agent'] = UserAgent().random

        proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }

        # 1. Change ip
        strt_time_tmp = time.time()
        check_url = 'http://httpbin.org/ip'
        my_ip_info = requests.get(check_url, proxies=proxies, headers=headers).json()
        my_ip = my_ip_info['origin'].split(',')[0].strip()
        print("########## MY IP : {} ##########".format(my_ip))
        print('my_ip proc time : {}'.format(time.time() - strt_time_tmp))

        # 2. Call api
        strt_time_tmp = time.time()
        translator = Translator(proxies=proxies)
        response = translator.translate(target_text, src='en', dest='ko')
        result = response.text
        print("Translator plain : {}".format(target_text))
        print("Translator translated : {}".format(result))
        print('Translator proc time : {}'.format(time.time() - strt_time_tmp))

    except Exception as e:
        result = str(e)
    finally:
        print('send_test_proxies proc time : {}'.format(time.time() - strt_time))

    return result


if __name__ == '__main__':
    result = send_test_proxies('I am AI')
    print('init result value : {}'.format(result))
    app.run(host="0.0.0.0", port=80)

    