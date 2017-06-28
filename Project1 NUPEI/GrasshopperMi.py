# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'


import matplotlib.pyplot as plt
import math, numpy
import pp
import time
import sys




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

def funcao_repeticao(n, m):

    lista3 = []

    for j in range(m):
        jump = funcao_pulo(n)

        soma1 = sum(jump[0])
        soma2 = sum(jump[1])

        distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)
        lista3.append(distancia_em_cada_simulacao)
        distancia_media = sum(lista3) / len(lista3)

    return distancia_media #plt.show()

print(funcao_repeticao(2,100000))

print "Time elapsed: ", time.time() - start_time, "s"