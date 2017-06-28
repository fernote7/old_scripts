# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'


import matplotlib.pyplot as plt
import math, numpy
import pp
import time
import sys




start_time = time.time()




def funcao_pulo(n):

    cosenos, senos = 0, 0


    for i in range(n):
        angulo = numpy.random.uniform(0, 2*numpy.pi)

        cosenos = math.cos(angulo)

        senos = math.sin(angulo)

    return cosenos, senos




#distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)
#print [soma1, soma2], distancia_em_cada_simulacao





def funcao_repeticao(n, m):

    lista3 = []

    for j in range(m):
        x, y = 0, 0

        jump = funcao_pulo(n)

        cosenos, senos = jump

        x += cosenos
        y += senos

        #soma1 = sum(jump[0])
        #soma2 = sum(jump[1])


        #distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)
        #r = [soma1, soma2]

        #lista3.append(distancia_em_cada_simulacao)
        #distancia_media = sum(lista3) / len(lista3)




    return x, y


a = funcao_repeticao(2, 100)

print a
b = a[0]
c = a[1]

plt.scatter(b,c)
plt.axis([-2, 2, -2, 2])
plt.grid(True)
plt. show()


ppservers = ()

if len(sys.argv) > 1:
    ncpus = int(sys.argv[1])
    job_server = pp.Server(ncpus, ppservers=ppservers)

else:
    job_server = pp.Server(ppservers=ppservers)

print "Starting pp with", job_server.get_ncpus(), "workers"

job1 = job_server.submit(funcao_repeticao, (2, 10),(funcao_pulo,), ("numpy", "math"))
#job2 = job_server.submit(funcao_repeticao, (2, 10),(funcao_pulo,), ("numpy", "math"))


result = job1()

print "Distance from origin is", result

#inputs = (2,)
#jobs = [(input, job_server.submit(funcao_repeticao), (input, 10000), (funcao_pulo,), ("math", "numpy",)) for input in inputs]
#for input, job in jobs:
#    print "Results for", input, "jumps are", job()



print "Time elapsed: ", time.time() - start_time, "s"
job_server.print_stats()









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
