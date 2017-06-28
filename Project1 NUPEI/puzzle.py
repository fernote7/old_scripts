__author__ = 'Fernando'

#def main(x):
#    return max(max_soma(x))

def max_soma(x):
    #print(x)
    if len(x) == 1:

        return (0, x[0])
    a, b = max_soma(x[:-1])
    #print (a,b)
    result = (max(a, b), x[-1] + a)

    return result

print(max(max_soma([2, 3, 12, 7])))

import itertools
from collections import OrderedDict

lista_2 = [2, 3, 12, 7]
subsets= []
for i in range(0, len(lista_2)+1):
  for subset in itertools.combinations(lista_2, i):
    subsets.append(subset)


#print (subsets)
#print (len(subsets))

'''
for i in range(len(lista)):
    teste = []
    for j in range(len(lista[i])):
        for k in stuff:
            if len(lista[i]) >= 2:
                if lista[i][j] == k:
                    teste.append(k)
                    if len(teste) == 2:
                        lista.remove(lista[i])
                        teste=[]

            else:
                pass

print(teste)
'''
#for i in subset:
#    if subset[]


def combinacao(subsets):
    somas = []
    for j in subsets:
        soma = sum(j)
        somas.append(soma)
    return somas

#print(combinacao(subsets))

'''
for tuple in subsets:
    for i in range(0, len(stuff)):
        for j in range(0,len(tuple)):
            if tuple[j] != stuff[i+j]:
                break
            if j == len(tuple) - 1:
                if len(tuple) < 2:
                    pass
                else:
                    print("We have a match at index",i, "to index", i+j, "which matches",tuple)
                    subsets.remove(tuple)
'''


list_1 = subsets

lista = lista_2
'''
removeElements = []
for k in range(len(list_1)):
    #if len(list_1[k]) == 0:        #Uncomment to delete empty set
    #    removeElements.append(k)
    for i in range(0, len(list_2)):
        for j in range(0, len(list_1[k])):
            if len(list_2) <= i + j:
                break
            if list_1[k][j] != list_2[i + j]:
                break
            if j == len(list_1[k]) - 1:
                print("removing", list_1[k])
                removeElements.append(k)

for i in range(len(removeElements)):
    list_1.pop(removeElements[i] - i)

print("List_1:", list_1)
'''
'''
y = [list(i) for i in list_1]
x = [list_2[0:2], list_2[1:3], list_2[2:4]]

new_list_1 = [tuple(i) for i in y if i not in x[0:]]
#print(new_list_1)


from itertools import islice

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

#print([t for t in list_1 if len(t) < 2 or t not in window(list_2, len(t))])
'''

print("Subsets:", subsets)
print("Lista:", lista)
removeElements = []
for k in range(len(subsets)):
    #if len(list_1[k]) == 0:
    #    removeElements.append(k)
    count = 0
    for i in range(0, len(lista)):
        for j in range(0, len(subsets[k])):
            if len(lista) <= i + j:
                break
            count = count + 1
            if subsets[k][j] != lista[i + j]:
                count = 0
            if count == 2:
                print("removing", subsets[k])
                removeElements.append(k)

removeElements = sorted(set(removeElements))
for i in range(len(removeElements)):
    subsets.pop(removeElements[i] - i)

print("List_1:", subsets)

maximos=[]
for elemento in subsets:
    soma=sum(elemento)
    maximos.append(soma)
print(max(maximos))