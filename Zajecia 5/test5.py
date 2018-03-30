#!/usr/bin/env python
#encoding: utf-8

import json

slownik={
	'k1':'w1',
	'k2':'w2',
	3:[1,2,3]
}

json_str=json.dumps(slownik)
print(json_str)
print(isinstance(json_str, basestring))
slownik2=json.loads(json_str)
print(slownik2.items())
