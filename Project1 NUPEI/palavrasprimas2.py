# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'

#z = [v for k, v in dicio.iteritems() if k in a]
#print z

def palavrasprimas():

    dicio = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
         'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
         'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37,
         'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49,
         'X': 50, 'Y': 51, 'Z': 52}

    r = ""

    frase = "Isso aqui eh Brasil"

    c = frase.split()


    for palavra in c:
        e = list(palavra)
        y = [dicio[x] for x in e]
        n = sum(y)

        divisores = []
        for i in range(n):
            i += 1

            if n % i == 0:
                divisores.append(i)


        if len(divisores) == 2:
            print "%s PALAVRA PRIMA de valor %d" %(e, n)
        else:
            print "%s PALAVRA NÃO PRIMA de valor %d" %(e, n)


    return r



print palavrasprimas()


#Just an example how the dictionary may look like
#myDict = {'age': ['12'], 'address': ['34 Main Street, 212 First Avenue'],
#          'firstName': ['Alan', 'Mary-Ann'], 'lastName': 'Stone'}

#Checking if string 'Mary' exists in dictionary value
#print 'Stone' in myDict.values()