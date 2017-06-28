__author__ = 'fernando.ormonde'


import matplotlib.pyplot as plt


u = 1.5
d = 0.5
S = 80
K = 80
r = 1.1
p = float((r-d))/(u-d)

print p

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial2(j):
    if j == 0:
        return 1
    else:
        return j * factorial(j - 1)

def factorial3(n, j):
    if (n-j) == 0:
        return 1
    else:
        return (n-j) * factorial((n-j) - 1)

def C(n):
    lista = []
    for j in range(0, n+1):
        e = float(factorial(n)/(factorial2(j)*factorial3(n,j))* p**j * (1-p)**(n-j) * max(0, u**j * d**(n-j) * S - K)
                  /r ** n)
        lista.append(e)

    g = sum(lista)
    print lista
    plt.plot(lista, 'ro-')
    plt.axis([0, 40, 0, 15])
    plt.show()
    return g

print C(50)
