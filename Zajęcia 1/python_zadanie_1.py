#Zadanie 5
#import os
#def gen(a):
#  for plik in os.listdir(a):
#    print(plik)
    
#gen("C:\")


#Zadanie 4
#punkty=[(1,1),(2,5),(-2,4),(-6,-6),(8,-9),(22,13),(-20,-40),(0,1)]
#punkt=(0,0)
#tab=[]

#def f1(p, punkt):
#  a=(p[0]-punkt[0])**2+(p[1]-punkt[1])**2
#  a=a**0.5
#  return a

#def f2(f, punkty, punkt, tab):
#  for x in punkty:
#    tab.append((f(x, punkt),x))

#f2(f1,punkty, punkt, tab)
#tab.sort()
#print(tab)


#Zadanie 3
#liczba=[1,2,3,4,5,6,7,8,9,10]
#po_warunku=[]

#def f1(n):
#  if(n%2==1):
#    return 0
#  else:
#    return 1
#
#def f2(f1, liczba):
#  for x in liczba:
#    if(f1(x)==1):
#      po_warunku.append(x)
#
#f2(f1, liczba)
#print(po_warunku)


#Zadanie 2 - awykonalne
#n=input('Podaj liczbe wyrazow ciagu ')
#fib=[]
#fib.append(1)
#fib.append(1)
##tab=[int((((1+5**) for x in range(1,n+1)]
#print(tab)


#Zadanie 1
#napis=input('Podaj napis')
#ls=[(slowo, len(slowo)) for slowo in napis.split()]
#print(ls)



#def generator(n):
#  while n:
#    print('Generator stop %d' %n)
#    yield n
#    print('Generator start %d' %n)
#    n=n-1

#for x in generator(5):
#  print('Wywolanie %d' %x)
##generator(5)



#kwadrat=lambda x: x*x
#print(kwadrat(2))




#def f1(n):
#  def f2(x):
#    return n-x
#  return f2

#res=f1(5)
#print(res(10))




#liczby=range(0,20)
#kwadraty=[x**2 for x in liczby]
#print (kwadraty)
