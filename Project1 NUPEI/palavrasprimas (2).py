# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'

dicio = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
         'z': 26}


frase = "deca"

c = frase.split()


palavra = "decaaa"


a = list(palavra)


#z = [v for k, v in dicio.iteritems() if k in a]

y = [dicio[x] for x in a]
n = sum(y)




#print z

print "A soma é de %d" %n

def primos(n):
    divisores = []
    for i in range(n):
        i += 1
        if n % i == 0:
            divisores.append(i)
    if len(divisores) == 2:
        print "PALAVRA PRIMA"
    else:
        print "PALAVRA NÃO PRIMA"


    return "os divisores são %s" %divisores


print primos(n)


#Just an example how the dictionary may look like
#myDict = {'age': ['12'], 'address': ['34 Main Street, 212 First Avenue'],
#          'firstName': ['Alan', 'Mary-Ann'], 'lastName': 'Stone'}

#Checking if string 'Mary' exists in dictionary value
#print 'Stone' in myDict.values()