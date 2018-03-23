#!/usr/bin/env python
#encoding: utf-8

import string

slownik={
}

import sys

p=5
line2=""

f2=open("plik2.txt", "w")

with open("plik.txt", "r") as f:
	for line in f:
		line2=""
		for c in line:
			if(c>='a'):
				if(c<='z'):
					c=chr(ord(c)+p)
					#c=c+str(p)
					if(c>'z'):
						c=c-'a'
			if(c>='A'):
				if(c<='Z'):
					c=chr(ord(c)+p)
					#c=str(int(c)+p)
					if(c>'Z'):
						c=c-'A'
			line2=line2+c
		f2.write(line2)
f2.close()
