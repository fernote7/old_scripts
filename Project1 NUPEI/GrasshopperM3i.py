# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'

import math, numpy
import time
from matplotlib.colors import LogNorm
import matplotlib as plt
from pylab import *
numpy.random.seed(1357)
start_time = time.time()


def funcao_pulo(n):
    #import pdb; pdb.set_trace() # n next line, c sai do loop, l lista onde está
    cosenos = []
    senos = []


    angulo = numpy.random.uniform(0, 2*numpy.pi)

    b = math.cos(angulo)
    cosenos.append(b)
    c = math.sin(angulo)
    senos.append(c)


    return cosenos, senos

def funcao_repeticao(n, m):

    lista3 = []
    posx = []
    posy = []

    for j in range(m):
        for i in range(n):
            jump = funcao_pulo(n)

            soma1 = sum(jump[0])
            soma2 = sum(jump[1])
            posx.append(soma1)
            posy.append(soma2)
            distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)
            lista3.append(distancia_em_cada_simulacao)
    distancia_media = sum(lista3) / len(lista3)
    #plt.scatter(posx, posy)
    hist2d(posx, posy, bins=60, norm=LogNorm())
    colorbar()

    return distancia_media, plt.show()




print(funcao_repeticao(2,10000))

print "Time elapsed: ", time.time() - start_time, "s"


