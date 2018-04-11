#!/usr/bin/env python
#encoding: utf-8

class Wyjatek(Exception):
	pass 
	
try:
	raise Wyjatek('Wystapil nieoczekiwany blad')
except Wyjatek as w:
	print(w)
