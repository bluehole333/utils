# /usr/bin/env python
# -*- coding: utf-8 -* 
import socket
import re


class MemcacheServer(object):
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host=None, port=None):
        self.host = host
        self.port = port
        try:
            self.server.connect((host, port))
        except:
            print("connect error ......")

    def send(self, msg):
        self.server.send(msg)

    def get_msg(self):
        buf_len = 1024
        msg = u""
        while True:
            buf = self.server.recv(buf_len)
            msg += buf
            if len(buf) != buf_len:
                break
        return msg


if __name__ == "__main__":
    ms = MemcacheServer()
    ms.connect("127.0.0.1", 11211)
    items = {}
    totalitems = 0
    ms.send("stats items\r\n")
    for line in ms.get_msg().splitlines():
        match = re.search("^STAT items:(\d*):number (\d*)", line)
        if match:
            i, j = match.groups()
            items[int(i)] = int(j)
            totalitems += int(j)

    for buckets in sorted(items.keys()):
        ms.send("stats cachedump %d %d\r\n" % (buckets, items[buckets]))
        for line in ms.get_msg().splitlines():
            match = re.search("^ITEM (\S+) \[.* (\d+) s\]", line)
            if match:
                print(match.groups()[0])
