__author__ = 'fernote7'


import time, math
import numpy as np
import matplotlib.pyplot as plt
from itertools import permutations
np.random.seed(1357)

def euclid_distance(A,c1,c2):
    x1,y1 = A[:,c1]
    x2,y2 = A[:,c2]
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)

def heavy_tails(N):
    L = list()
    for i in range(N):
        f = np.random.random()
        while 0.2 < f < 0.8:
            f = np.random.random()
        L.append(f)
    return L

def init(N=10):
    D = dict()
    if True:
        A = np.random.uniform(size=N*2)
    else:
        A = [np.random.random() for n in range(N)]
        L = heavy_tails(N)
        A = np.array(A + L)
    A.shape = (2,N)
    for L in A:
        L = [str(round(e,3)).ljust(5) for e in L]
        for e in L:  print e + ' ',
        print
    print
    for c2 in range(A.shape[1]):
        for c1 in range(c2):
            D[(c1,c2)] = euclid_distance(A,c1,c2)
    return A,D

def show_distances(A,D):
    for k in sorted(D.keys()):
        print k, str(round(D[k],2))
    print

def repr(L,dist):
    rL = [' '.join([str(n) for n in L]) + '  ']
    rL.append(str(round(dist,3)))
    return '\n'.join(rL)

def try_random(N,D):
    L = range(N)
    np.random.shuffle(L)
    return repr(L,total_distance(L,D))

def total_distance(L,D,n=None):
    d = 0
    for first,next in zip(L[:-1],L[1:]):
        if first < next:
            d += D[(first,next)]
        else:
            d += D[(next,first)]
        if n and d > n:
            return None
    return d

'''
def partOne():
    N = 6
    A,D = init(N)
    show_distances(A,D)
    #plot(A,D)
    for i in range(5):
        result = try_random(N,D)
        print result
'''


def try_all(N,D):
    smallest = N*1
    retval = None
    for i,L in enumerate(permutations(range(N))):
        dist = total_distance(L,D)
        if dist < smallest:
            smallest = dist
            print 'i =', str(i).rjust(7),
            print 'new smallest =', round(smallest,3)
            retval = repr(L,dist)
    return retval

def branch_and_bound(N,D):
    smallest = N*1
    retval = None
    for L in permutations(range(N)):
        dist = total_distance(L,D,n=smallest)
        if not dist:  continue
        if dist < smallest:
            smallest = dist
            retval = repr(L,dist)
    return retval


def partTwo():
    N = 10
    A,D = init(N)
    #plot(A,D)
    print 'N = ', N
    print math.factorial(N), 'possibilities'
    then = time.time()
    retval = try_all(N,D)
    now = time.time()
    print
    print 'min'
    print retval
    print round(now-then,4), 'sec'
    then = now
    retval = branch_and_bound(N,D)
    now = time.time()
    print retval
    print round(now-then,2), 'sec'


print(partTwo())