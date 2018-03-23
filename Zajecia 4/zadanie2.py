#!/usr/bin/env python
#encoding: utf-8

slownik={
}

import sys

f=open(sys.argv[1])

for x in f:
	wyrazy=x.split(":")
	wyraz=wyrazy[1].split("\n")
	wyrazy[1]=wyraz[0]
	slownik[wyrazy[0]]=wyrazy[1]

f.close()

print slownik
