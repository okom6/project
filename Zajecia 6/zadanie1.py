#!/usr/bin/env python
#encoding: utf-8

def divide(x, y):
	try:
		result=x/y
	except (ZeroDivisionError, TypeError) as ex:
		print('Wyjatek - dzielenie przez zero')
		print(ex)
	else:
		print('Brak wyjatku')
		return result
	finally:
		print('Koniec funkcji')

print(divide(4,'test'))
