#!/usr/bin/env python
#encoding: utf-8

import urllib2

response=urllib2.urlopen('http://python.org/')
html=response.read()
print html

#
