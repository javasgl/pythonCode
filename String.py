#!/usr/bin/env python
#-*-coding:utf8-*-
en='ABC'.encode('ascii');
print(en);
zh='中文'.encode('utf8');
print(zh);
#err ='中文'.encode('ascii');
#print(err)
#string to bytes encode
#bytes to string decode
print(b'ABC'.decode('ascii'));
#中文转byte,byte转string
print('中文'.encode('utf8').decode('utf8'));

#格式化
print('hi,%s,your %s score is %d,and %.2f%%'%('word',False,26,23.9));
