from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import NUMERIC
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import ForeignKey

Base = declarative_base()

class Czytelnicy(Base):
    __tablename__ = 'czytelnicy'
    id_czytelnik = Column(Integer, primary_key=True)
    imie = Column(String(100))
    nazwisko = Column(String(100))
    adres = Column(String(100))

class Autorzy(Base):
    __tablename__ = 'Autorzy'
    id_autor = Column(Integer, primary_key=True)
    imie = Column(String(100))
    nazwisko = Column(String(100))
    
class Ksiazki(Base):
    __tablename__ = 'ksiazki'
    id_ksiazka = Column(Integer, primary_key=True)
    tytul = Column(String(100))
    id_autor = Column(Integer, ForeignKey("Autorzy.id_autor"))
    signature = Column(String(100))


engine = create_engine('sqlite:///biblioteka2.db',echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session=Session()

for autor in session.query(Autorzy).all():
    print(autor.id_autor, autor.imie, autor.nazwisko)
  
def dodaj_ksiazke(id, t, id_aut, syg):
    new_book = Ksiazki(id_ksiazka = id, tytul = t, id_autor = id_aut, signature = syg)
    session.add(new_book)
    
dodaj_ksiazke(2, 'Potop', 1, 'hsffy334')

for ksiazka in session.query(Ksiazki).all():
    print(ksiazka.id_ksiazka, ksiazka.tytul, ksiazka.id_autor, ksiazka.signature)
#session.commit()