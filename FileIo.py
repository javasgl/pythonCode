#!/usr/bin/env python3
#-*-encoding:utf8-*-

try:
	f=open('./FileIo.py','r');
	print(f.read());
except Exception as e:
	raise
finally:
	f.close();

#自动处理关闭
with open('./FileIo.py','r') as f:
	print(f.read());

#读取一行
with open('./FileIo.py','r') as f:
	for line in f.readlines():
		print(line.strip());

with open('./FileIo.py','w'):
	f.write('Hello World!');