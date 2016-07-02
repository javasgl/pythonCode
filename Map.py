#!/usr/bin/env python3
#-*-encoding:utf8-*-

m ={'s':100,'g':19,'i':8,'i':7};
print(m['s']);
print(m.get('c'));
print(m.get('d','默认值'));
if('e' in m):
	print('in dict');
else:
	print('not in dict');	
	m['e']='add';
	print(m);

for k,v in m.items():
	print('%s==%s'%(k,v));

for v in m.values():
	print(v);

#enumerate可以将list转化为key=>value的list
for k,v in enumerate(range(10)):
	print('%s==%s'%(k,v));
#将list中元素小写
upCaseList=['Java','Python3','Php','Golang','Js'];
print([s.lower()for s in upCaseList]);
#list 含有数字
upCaseList=['Java','Python3','Php',29,'Golang','Js'];
print([s.lower()for s in upCaseList if isinstance(s,str)]);
print(upCaseList);

#lambda表达式
lam = lambda x:x*x;
#map
print(map(lam,[1,2,3]));
#reduce
print(reduce(lambda x,y:y+x,map(lam,[1,2,3])));

