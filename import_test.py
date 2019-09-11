#-*- coding: utf-8 -*-
"""
递归导入
"""
import os
import os.path
import sys

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
settings.configure()
cur_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(cur_dir, ".."))


file_list = ['import_test', 'vendor', 'logs', 'xadmin']


def run_dir(py_dir):
    for root, dirs, files in os.walk(py_dir):
        for f in files:
            name, ext = os.path.splitext(f)
            print name, ext
            if ext == '.py' and name not in file_list:
                root = root.replace(py_dir, '').replace('/', '.').replace('\\', '.').replace('.', '')
                # print 'root:', root, 'name', name
                if root:
                    __import__(root, globals(), locals(), [name], -1)
                else:
                    __import__(name, globals(), locals(), [], -1)
    print "\n\n"
    print "OK No problem"
    print "\n"
    
if __name__ == '__main__':
    now_dir = os.getcwd()
    run_dir(now_dir)
