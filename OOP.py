#!/usr/bin/env python3
#-*-encoding:utf8-*-

'oop'
__author__='songgl'

class Stu(object):
	def __init__(self,name,score=100):
		self.name=name;
		self.score=score;
	def print_score(self):
		print('%s:%s'%(self.name,self.score));

stu = Stu('song',99);
stu.print_score();
#dir打印属性和方法
for attr in dir(stu):
	print(attr+'\n');

for attr in dir('ABC'):
	print(attr+'\n');

print(__author__);
print(__doc__);
