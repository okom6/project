#!/usr/bin/env python
#encoding: utf-8

slownik={
}

import sys

if(sys.argv[2]!="-"):
	with open(sys.argv[1], "r") as f:
		for line in f:
			if(line.find(sys.argv[2])!=-1):
				print line
else:
	sys.argv
	pob=""
	while(pob!=" "):
		z=input()
		pob=pob+z
	print pob
