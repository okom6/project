#!/usr/bin/env python
#encoding: utf-8

napis='   TEST   '
print (napis)
print(napis.strip())
print(napis.strip().center(30))
print(napis.strip().capitalize())
print(napis.lower())
print(napis.lower().islower())
napis=napis.strip()
print(napis.startswith('TESTa'))
print(napis.ljust(30))
