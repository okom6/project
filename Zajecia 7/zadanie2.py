 #!/usr/bin/env python
#encoding: utf-8

import sqlite3

connection=sqlite3.connect('example3.db')
cursor=connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS test (id integer, title text, author text)''')


cursor.execute('''INSERT INTO test VALUES (1, 'O obrotach sfer niebieskich', 'Kopernik')''')
cursor.execute('''INSERT INTO test VALUES (2, 'Romeo i Julia', 'Sheakespear')''')

#connection.commit()
connection.rollback()

for row in cursor.execute('SELECT * FROM test'):
    print row


connection.close()
