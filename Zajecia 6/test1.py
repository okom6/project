 #!/usr/bin/env python
#encoding: utf-8

from xml.dom import minidom
import urllib2

response=urllib2.urlopen('https://www.yr.no/sted/Polen/Lublin/Lublin/forecast.xml')
doc=minidom.parse(response)
elements=doc.getElementsByTagName("sun")

for el in elements:
	attr=el.getAttribute("rise")
	print attr
