#!/usr/bin/env python3
#-*-encoding:utf8-*-
arr =['a','b','c'];
print(arr);
print(arr[1]);
print(arr[-1]);#取倒数第N个
arr.append('d');
print(arr);
arr.insert(2,'direct insert');
print(arr);

pop = arr.pop(); #队尾元素
print(pop);
print(arr);
pop = arr.pop(-1); #指定元素
print(pop);
print(arr);

newArr =('a','b','c'); #指向不可变不可修改的list
print(newArr);
print(newArr[1]);

#定义只有一个元素的tuple
print((1,));
print((1));

#循环
newArr=['go','to','school'];
for item in newArr:
	print(item);

print(list(range(6))); #[0...5]
sum=0;
for num in range(101): #[0...100]
	sum+=num;
print(sum);

sum=0;
n=99;
while(n>0):
	sum+=n;
	n-=2;
print(sum);


