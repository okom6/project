#!/usr/bin/env python
#encoding: utf-8

import re
import sys;

regex_ip=re.compile(
	r'''(?P<IP>\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d
	)''',
	re.IGNORECASE | re.VERBOSE
)

with open("plik2.txt", "r") as f:
	for line in f:
		#print(line)
		for match_object in regex_ip.finditer(line):
			print match_object.groupdict()
