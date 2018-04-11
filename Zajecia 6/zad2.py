#!/usr/bin/env python
#encoding: utf-8

import re

class Mail(Exception):
	adres=[]
	def __init__(self, a):
		if not re.match('[^@]+@[^@]+\.[^@]+', a):
			raise Exception("Niepoprawny a-mail")
		else:
			self.adres.append(a)

m=Mail('ala@gmail.com')
