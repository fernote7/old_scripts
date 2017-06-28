__author__ = 'fernando.ormonde'



def primos(n):
    divisores = []
    nao_dividem = []
    for i in range(n):
        i += 1
        if n % i == 0:
            divisores.append(i)
        else:
            nao_dividem.append(i)

    if len(divisores) == 2:
        print "PRIMO"
    else:
        print "NAO PRIMO"


    return divisores

print primos(19)


import Primos2
