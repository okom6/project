#!/usr/bin/env python
#encoding: utf-8

slownik={
}

napis="'k1:w1, k2:w2, k3:w3'"

podzial=napis.split(", ")

for x in podzial:
	wyrazy=x.split(":")
	slownik[wyrazy[0]]=wyrazy[1]

print slownik
