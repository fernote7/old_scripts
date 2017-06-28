# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'


import matplotlib.pyplot as plt
import math, numpy
import pp
import time
#import sys




start_time = time.time()




def funcao_pulo(n):

    cosenos = []
    senos = []

    for i in range(n):
        angulo = numpy.random.uniform(0, 2*numpy.pi)

        b = math.cos(angulo)
        cosenos.append(b)
        c = math.sin(angulo)
        senos.append(c)


    return cosenos, senos




#distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)
#print [soma1, soma2], distancia_em_cada_simulacao





def funcao_repeticao(n, m):

    lista3 = []

    for j in range(m):
        jump = funcao_pulo(n)

        soma1 = sum(jump[0])
        soma2 = sum(jump[1])

        distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)
        #r = [soma1, soma2]

        plt.scatter(soma1, soma2)
        plt.axis([-2, 2, -2, 2])
        plt.grid(True)
        plt.set_cmap('hot')


        lista3.append(distancia_em_cada_simulacao)
    distancia_media = sum(lista3) / len(lista3)


    return distancia_media, plt.show()



'''
ppservers = ()


if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    job_server = pp.Server(ncpus, ppservers=ppservers)

else:
    job_server = pp.Server(ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"

job1 = job_server.submit(funcao_repeticao, (100, 40000),(funcao_pulo,), ("numpy", "math", "matplotlib.pyplot"))
job2 = job_server.submit(funcao_repeticao, (500, 40000),(funcao_pulo,), ("numpy", "math", "matplotlib.pyplot"))


result = job1(), job2()
'''


print("Distance from origin is", funcao_repeticao(2,1000))

#inputs = (2,)
#jobs = [(input, job_server.submit(funcao_repeticao), (input, 10000), (funcao_pulo,), ("math", "numpy",)) for input in inputs]
#for input, job in jobs:
#    print "Results for", input, "jumps are", job()



print "Time elapsed: ", time.time() - start_time, "s"
#job_server.print_stats()










#ppservers = ()

#if len(sys.argv) > 1:
#    ncpus = int(sys.argv[1])
#    job_server = pp.Server(ncpus, ppservers=ppservers)

#else:
#    job_server = pp.Server(ppservers=ppservers)

#print "Starting pp with", job_server.get_ncpus(), "workers"

#job1 = job_server.submit(funcao_pulo, (1000, 1000),(), ("numpy", "math"))


#result = job1()

#print "Sum of primes below 100 is", result

#inputs = (10,)
#jobs = [(input, job_server.submit(funcao_pulo,(input, 2), (), ("math", "numpy"))) for input in inputs]
#for input, job in jobs:
#    print "Results", input, "are", job()



#print "Time elapsed: ", time.time() - start_time, "s"
#job_server.print_stats()



# Define your jobs
#job1 = job_server.submit(funcao_pulo, (1000,), (1000,))
#job2 = job_server.submit(funcao_pulo, (1000,), (1000,))

# Compute and retrieve answers for the jobs.
#print job1()
#print job2()


#plt.show()
