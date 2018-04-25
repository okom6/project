#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

dirStr='''K1
	K2
	K3
		K4
K5
	K6'''

komenda="mkdir"
s1=""
s2=""
s3=""
l=0

for i in dirStr :
	if(i!="\t"):
		if(i!="\n"):
			if(i!="K"):
				print(l)
				if(l==0):
					s1=i
					komenda=komenda+" K"+s1
				elif(l==1):
					s2=i
					komenda=komenda+" K"+s1+"/K"+s2
				else:
					s3=i
					komenda=komenda+" K"+s1+"/K"+s2+"/K"+s3
				l=0
	else:
		l=l+1

subprocess.check_output([komenda], shell=True)
