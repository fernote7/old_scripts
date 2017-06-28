# -*- coding: utf-8 -*-
__author__ = 'fernando.ormonde'

import numpy as np
import matplotlib.pyplot as plt
import math as math
import time
import numba

a=time.time()

#@numba.jit(nopython=True)
def funcao_pulo(n, m):
    lista3 = []

    for j in range(m):
        cosenos = []
        senos = []
        for i in range(n):
            angulo = np.random.uniform(0, 2 * np.pi)

            b = math.cos(angulo)
            cosenos.append(b)

            c = math.sin(angulo)
            senos.append(c)

            soma1 = sum(cosenos)
            soma2 = sum(senos)

            distancia_em_cada_simulacao = (soma1 ** 2 + soma2 ** 2) ** (1. / 2)

        r = [soma1, soma2]

        lista3.append(distancia_em_cada_simulacao)

        distancia_media = sum(lista3) / len(lista3)

        # plt.plot(soma1, soma2)
        # plt.axis([-2, 2, -2, 2])
        # plt.grid(True)
        # plt. show()

    return distancia_media


print funcao_pulo(100, 10000)


b=time.time()

tempo = b-a

print(tempo)

# plt.show()
