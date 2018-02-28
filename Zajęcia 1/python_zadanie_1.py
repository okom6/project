#Zadanie 5
n=input('Wprowadz liczbe liczb ')
lista=[]

i=0
while(i<int(n)):
	lista.append(input())
	i=i+1

lista.sort()

kierunek=input('Wprowadz kierunek sortowania: 0-rosnaco, 1-malejaca')
zakres=input('Podaj ilosc wypisywanych elementow')

if(int(kierunek)==1):
	lista.reverse()

k=0
for i in lista:
	if(k<int(n)):
		print(i)
	k=k+1



#Zadanie 4
#lista=['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
#alfabet=''
#skok=input('Wprowadz liczbe ')

#l=1
#for i in lista:
#	if(l%skok==0):
#		alfabet=alfabet+i
#	l=l+1
#print(alfabet)


#Zadanie 3
#lista=['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
#alfabet=''

#for i in lista:
#	alfabet=alfabet+i
  
#print(alfabet)

#Zadanie 2
#a=input('Wprowadz liczbe ')
#b=input('Wprowadz liczbe ')
#c=input('Wprowadz liczbe ')

#if(a>b):
#  if(a>c):
#    print(a)
#  else:
#    print(c)
#else:
#  if(b>c):
#    print(b)
#  else:
#    print(c)


#Zadanie 1
#imie=input('Wprowadz imie')
#nazwisko=input('Wprowadz nazwisko')
#wiek=int(input('Wprowadz wiek'))

#if(wiek>17):
#  print('Czesc '+imie+' '+nazwisko+' jestes Pelnoletni')
#else:
#  print('Czesc '+imie+' '+nazwisko+' jestes Niepelnoletni')

##############
#lista=[1,2,3,'a',4,5]
#lista[1]=8
#print(lista)

#krotka=[1,2,3,'a',4,5]
#krotka[1]=8
#print(krotka)


#;


#li=['a','b','c','d']

#for i in range(len(li)):
#  print(li[i])

#for i in li:
#  print(i)

#i=0
#while(i<5):
#  print(i)
#  i=i+1

#;

#a=2 
#b=3
#if(a>b):
#  print('wieksze')
#elif(a<b):
#  print('mniejsze')
#else:
#  print('rowne')

#;

#def suma(a,b):
#  return a+b

#l1=3
#l2=4

#print(suma(l1, l2))

#;

#l1=3
#l2=4.5
#t1='6'

#print(l1)
#print(l2)
#print(t1)

#;

#data=input('Wprowadz dane')
#print(data)