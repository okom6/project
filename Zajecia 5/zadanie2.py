#!/usr/bin/env python
#encoding: utf-8

import sys

licznik_max=int(sys.argv[1])
l=0
string=""

with open("plik1.txt", "r") as f:
	for line in f:
		for x in line:
			if(l==licznik_max):
				l=0
				print(string.center(licznik_max))
				string=""
			string=string+x
			l=l+1




