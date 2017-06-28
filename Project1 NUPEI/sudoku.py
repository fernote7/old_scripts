# -- coding: utf-8 --
__author__ = 'fernote7'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

digits   = '123456789'
rows     = 'ABCDEFGHI'
cols     = digits
squares  = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

'''
pega cada elemento em 'squares' (todos os elementos do jogo) e transforma em uma chave de dicionário. Procura por este
elemento nas listas do objeto 'unitlist' (com todas as combinações possíveis) e retorna como valor para esta chave.
'''
units = dict((s, [u for u in unitlist if s in u])
             for s in squares)

'''
Mesma estrutura que o objeto units, porém não associando valores repetidos a uma chave (estrutura de set)
'''
peers = dict((s, set(sum(units[s],[]))-set([s]))
             for s in squares)

#print(squares)
#print(unitlist)
#print(units)
print(peers)


n = 1.

print((n).is_integer())