__author__ = 'fernando.ormonde'


#import numpy as np
#import timeit
#import matplotlib.pyplot as plt

lista = []



def primos(n):
    lista = []

    i = 0

    while i <= n:

        i+=1
        divisores = []

        for j in range (i):
            j += 1
            if i % j == 0:
                divisores.append(j)


        if len(divisores) == 2:
            lista.append(i)




    return lista


print primos(10)
print len(primos(10))


#import time
#import timeit

#def simple_timer(primos, n):
#    start = time.clock()

#    return time.clock() - start


#print simple_timer(primos, 10000)






#plt.plot(primos(1000))
#plt.xlabel('Nao sei')
#plt.ylabel('tb nao')



#plt.show()

