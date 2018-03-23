#!/usr/bin/env python
#encoding: utf-8

slownik={
"k1":"w1",
"k2":"w2",
2: [1,2,3],
(4,3,2):4,
}
#slownik["slownik"]=slownik

#print slownik.get("k3","dom")
#print slownik.get("k1")

for x in slownik.values():
	print x
