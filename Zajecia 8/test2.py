#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

with open(os.devnull, 'w') as devnull:
    out1=subprocess.call(["echo Hello World!"], stderr=devnull, shell=True)

try:
    out2=subprocess.check_output(["echo Hello World!"], shell=True)
except subprocess.CalledProcessError as ex:
    print ex
