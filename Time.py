#!/usr/bin/env python3
# -*-encoding:utf8-*-


from datetime import datetime;

# 当前时间
print(datetime.now());

print(datetime(2016, 12, 12, 12, 12, 12));

print(datetime.now().timestamp());
print(datetime.fromtimestamp(datetime.now().timestamp()));
# strtotime
print(datetime.strptime('2016-12-02 19:23:28', '%Y-%m-%d %H:%M:%S'));

# time to string
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'));
