 #!/usr/bin/env python
#encoding: utf-8

from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base=declarative_base()

class Test(Base):
    __tablename__='test2'
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    value=Column(NUMERIC)
    
class Student(Base):
    __tablename__='test3'
    id=Column(Integer, primary_key=True)
    name=Column(String(100))
    book_id=Column(Integer)
    
engine=create_engine('sqlite:///example3.db', echo=True)

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

#for test in session.query(Test).all():
#    print (test.id, test.name, test.value)
    
new_data2=Student(
    id=1,
    name=u'Adam',
)
#session.commit()
new_data=Test(
    id=1,
    name=u'O obrotach sfer niebieskich',
    value=20.9
)

session.add(new_data)

new_data=Test(
    id=2,
    name=u'Romeo i Julia',
    value=30.9
)
session.add(new_data)
#
