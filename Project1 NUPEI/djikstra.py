__author__ = 'Fernando'

grafo = {'a':{'b': 1, 'e': 4, 'f': 8}, 'b':{'c': 2, 'g': 6, 'f': 6}, 'c':{'d': 1, 'g': 2}, 'd':{'g': 1, 'h': 4},
         'e':{'f': 5,}, 'g':{'f': 1, 'h': 1}}



def djik(grafo, chave):
    init = chave
    grafo = grafo

    for i in grafo.keys():
        if grafo.keys() == init:
            print(grafo.keys())

    return init


print(djik(grafo, 'd'))