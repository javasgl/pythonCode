#!/usr/bin/env python3
#-*-encoding:utf8-*-

class Dict(dict):
	def __init__(self,**kw):
		super().__init__(**kw);
	def __getattr__(self,key):
		try:
			return self[key];
		except KeyError as e:
			raise AttributeError(r"'Dict' 中不存在这个属性：'%s'"%key);
	def __setattr__(self,key,value):
		self[key]=value;