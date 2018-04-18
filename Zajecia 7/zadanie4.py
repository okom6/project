 #!/usr/bin/env python
#encoding: utf-8

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Book(Base):
    __tablename__='book'
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    value=Column(NUMERIC)
    
class Student(Base):
    __tablename__='student'
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    book_id=Column(Integer)
    
engine=create_engine('sqlite:///example4.db', echo=True)

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()
    
new_data2=Student(
    id=1,
    name=u'Adam',
    book_id=1
)
#
#session.add(new_data2)
new_data=Book(
    id=1,
    name=u'O obrotach sfer niebieskich',
    value=20.9
)

#session.add(new_data)

#session.commit()

for data1 in session.query(Student).all():
    print (data1.id, data1.name, data1.book_id)
    
for data1 in session.query(Book).all():
    print (data1.id, data1.name, data1.value)
