# -*- coding: utf-8 -*-
import threading
import time, urllib2

url = 'https://baidu.com'


def worker():
    try:
        response = urllib2.urlopen(url)
        print(response.getcode())
    except urllib2.HTTPError as e:
        print(e)


for i in range(3):
    t = threading.Thread(target=worker)
    t.start()
