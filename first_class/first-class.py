import numpy as np

# 1 par ou impar

x = 25
if x % 2 == 0:
    print("eh par")
else:
    print("eh impar")

# 2 maior numero da lista

lista = [ -10, 10, 0, 1, 1, 7, 11, 5, 4, 3 ]
maior = lista[0]
for n in lista:
    if n > maior:
        maior = n
print(maior)

# 3 somatorio da lista

lista = [ -10, 10, 0, 1, 1, 7, 11, 5, 4, 3 ]
total = 0
for i in lista:
    total += i
print(total)

# 4 Fibonacci

def F():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

print("Fibonacci seq:")
for i in SubFib(0, 34):
    print (i)

# 5 99 Bottles of Beer

beers = 99
word = "bottles"
count = 0
while (count < 99):
   if beers == 1:
       word = "bottle"

   print beers, word, "of beer on the wall"
   print beers, word, "of beer"
   print "Take one down!"
   print "Pass it around."
   if beers == 1:
       print "there are no more beer on the wall"

   beers = beers - 1
   count = count + 1


# numpy

print "-------------------"
print "usando funcoes numpy"
print "-------------------"

lista = [ -10, 10, 0, 1, 1, 7, 11, 5, 4, 3 ]

# 1 maior numero da lista
maior = np.amax(lista)
print "maior numero da lista numpy", maior

# 2 soma da lista
somatorio = np.sum(lista)
print "somatorio da lista numpy", somatorio

# 3 desvio padrao
desvio = np.sqrt(np.var(lista))
print "desvio padrao da lista numpy", desvio