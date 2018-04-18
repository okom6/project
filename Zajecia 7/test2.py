 #!/usr/bin/env python
#encoding: utf-8

import sqlite3

connection=sqlite3.connect('example.db')
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test (id integer, name text, value
real)''')


cursor.execute('''INSERT INTO test VALUES (1, 'TEST', 1.3)''')

connection.commit()

for row in cursor.execute('SELECT * FROM test'):
    print row


connection.close()
