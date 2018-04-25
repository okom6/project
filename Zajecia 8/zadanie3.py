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

for(i=0; i<dirStr.size(); ++i):
    if(dirStr[i]!="/t"):
        if(l==0)
            s1=dirStr[i]
            komenda=komenda+" "+s1
        elif(l==1)
            s2=dirStr[i]
            komenda=komenda+" "+s1+"/"+s2
        else:
            s1=dirStr[i]
            komenda=komenda+" "+s1+"/"+s2+"/"+s3
        l=0
    else:
        ++l
        

subprocess.check_output([komenda], shell=True)
