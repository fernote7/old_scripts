# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'



lista = [-1, 1]
lista3 = [2, 3, -1]

a = len(lista)



def valor_minimo(n):

    x = []
    for elemento in n:
        if x == []:
            x.append(elemento)
        elif x[0] > elemento:
            x.pop()
            x.append(elemento)

    return x



def valor_maximo(n):
    x = []
    for elemento in n:
        if x == []:
            x.append(elemento)
        elif x[0] < elemento:
            x.pop()
            x.append(elemento)

    return x




def valor_medio(n):
    if len(n) == 0:
        return 0
    else:
        z = float(sum(n))/len(n)

    return z




def stat(n):
    media = valor_medio(n)

    maximo = valor_maximo(n)
    maximo2 = int(float("%s"*len(maximo) % tuple(maximo)))
    minimo = valor_minimo(n)
    minimo2=int(float("%s"*len(minimo) % tuple(minimo)))

    return "Os valores maximo, minimo e medio sao, respectivamente, %d, %d e %d" %(maximo2, minimo2, media)

print stat(lista)

