#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

liczba = int(raw_input())
i=0
p=2
czy=1

while(liczba!=1):
    print("A")
    i=0
    czy=0
    for x in range(2, p):
        print("B")
        if(p%x==0):
            czy=1
            break
        
    if(czy==0):
        while(liczba%p==0):
            print("C")
            liczba=liczba/p
            i=i+1
            
    print("("+p+","+str(i)+")")
