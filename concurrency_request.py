# -*- coding: utf-8 -*-
import threading
import time
import ssl
import urllib.request

url = 'https://baidu.com'


def worker():
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    print(response.getcode())
    print(dir(response))
    response.read()


for i in range(30):
    t = threading.Thread(target=worker)
    t.start()
