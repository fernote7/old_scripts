__author__ = 'fernando.ormonde'


import numpy as np
from numpy import linalg

a=np.matrix([[1.,0.,0.],[-1.,1.,0.],[-1.,0.,1.]])




at = a.I




A = np.matrix([[0., 0., 0., 1.],[1.,1.,1., 1.],[8.,4.,2., 1.],[27.,9.,3., 1.]])

b = np.matrix([[1.], [0.], [-1.], [2.]])



c = linalg.solve(A, b)

print c

x = A.I * b

print x