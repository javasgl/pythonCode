#!/usr/bin/env python
def hello(a,b,*c,**kwargs):
    print a,b,c,kwargs

hello("first","second")
hello("first","second","third","fourth",order="asc",group="admin")
