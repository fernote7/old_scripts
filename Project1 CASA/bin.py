__author__ = 'Fernando'

lista = []
lista2 = []

def binario(n):
    a = n / 2
    b = n % 2
    lista.append(b)
    lista2.append(a)
    if a < 2:
        lista.append(a)
        return lista
    else:
        c=lista2[0]
        while c>1:
            d= c%2
            c= c/2
            lista.append(d)
        lista.append(c)
        return lista [::-1]

f = binario(20)
print f
r="%s"*len(f) % tuple(f)
print r

j= [str(x) for x in lista][::-1]
["".join(j)]
m=[int("".join(j))]
print m[0]