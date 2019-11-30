#!/bin/bash
# 每秒某个ip的访问上限
# iptables -L -n -v --line-numbers
num=100
list=`netstat -an |grep ^tcp.*:80|egrep -v 'LISTEN|127.0.0.1'|awk -F"[ ]+|[:]" '{print $6}'|sort|uniq -c|sort -rn|awk '{if ($1>$num){print $2,$1}}'`

for i in $list
do
      echo $i
      iptables -I INPUT -s $i --dport 80 -j DROP
done