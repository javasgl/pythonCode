#!/usr/bin/env python3
#-*-encoding:utf8-*-
import unittest;
from myDict import Dict;

class TestDict(unittest.TestCase):
	def test_init(self):
		d= Dict(a=1,b='test');
		self.assertEqual(d.a,1);
		self.assertEqual(d.b,'test');
		self.assertTrue(isinstance(d,dict));

	def test_key(self):
		d = Dict();
		d['key']= 'value';
		self.assertEqual(d.key,'value');

	def test_attr(self):
		d = Dict();
		d.key = 'value';
		self.assertEqual(d['key'],'value');

	def test_keyword(self):
		d = Dict();
		with self.assertRaises(KeyError):
			value=d['empty'];

	def test_attrerrot(self):
		d = Dict();
		with self.assertRaises(AttributeError):
			value=d.empty;
	#每个测试方法之前、之后执行		
	def setUp(self):
		print('start to test....connet db');
	def tearDown(self):
		print('end test!close db');
