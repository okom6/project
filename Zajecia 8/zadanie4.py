#!/usr/bin/env python
#encoding: utf-8

import sys

liczba=int(sys.argv[1])
i=0
p=2
tab=[]

while(liczba!=1):
	i=0     
	while(liczba%p==0):
		liczba=liczba/p
		i=i+1

	if(i>0):
		tab.append((p,i))
	p=p+1

print(tab)
