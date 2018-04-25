#!/usr/bin/env python
#encoding: utf-8

import subprocess
import os

try:
    out2=subprocess.check_output(["g++ -o pomoc1 pomoc1.cpp"], shell=True)
except subprocess.CalledProcessError as ex:
    print("Błąd kompilacji")
