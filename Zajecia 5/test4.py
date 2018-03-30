#!/usr/bin/env python
#encoding: utf-8

import re

regex_email=re.compile(
	r'''(?P<adres>
		(?P<login>[\w+.]+)
		@
		(?P<domena>\w+(\.\w+)+)
	)''',
	re.IGNORECASE
)

tekst=u'mail@gmail.com, "jan.nowak@poczta.pl"'
for match_object in regex_email.finditer(tekst):
	print match_object.groupdict()
