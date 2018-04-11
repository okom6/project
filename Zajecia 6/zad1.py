#!/usr/bin/env python
#encoding: utf-8


def pierwiastek(x):
	try:
		result=x**0.5
	except (TypeError):
		print('Niepoprawny typ.')
	except (ValueError):
		print('Liczba nie moze byc ujemna')
	except (NameError):
		print('Argument powinien byc liczba')
	else:
		return result

print(pierwiastek(3))

#obsluzyc wyjadki podczas obliczania pierwiastka
