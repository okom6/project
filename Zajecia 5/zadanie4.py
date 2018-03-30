#!/usr/bin/env python
#encoding: utf-8

import re
import sys;

regex_ip=re.compile(
	r'''(?P<PESEL>\d\d\d\d\d\d\d\d\d\d\d
	)''',
	re.IGNORECASE | re.VERBOSE
)

with open("plik3.txt", "r") as f:
	for line in f:
		for match_object in regex_ip.finditer(line):
			p=match_object.string[match_object.start(0):match_object.end(0)]
			if(int(p[9])%2==1):
				print (p[4]+p[5]+"-"+p[2]+p[3]+"-19"+p[0]+p[1]+" mężczyzna")
			else:
				print (p[4]+p[5]+"-"+p[2]+p[3]+"-19"+p[0]+p[1]+" kobieta")
