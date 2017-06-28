__author__ = 'fernando.ormonde'

import numpy as np
import matplotlib.pyplot as plt

def soma(x,y):
    return x+y

def produto(x,y):
    return x*y

#print soma(2,3)

#print produto(7, 32)

a = np.matrix('[2]; [3]')

#print a

plt.plot([1,8,3,4])
plt.ylabel('some numbers')
plt.xlabel('testing')
#plt.show()


def fizzbuzz(x):
    return '1'

import unittest
class FizzbuzzTests(unittest.TestCase):

    def test_retorna_1_ao_receber_1(self):
        self.assertEqual(fizzbuzz(1), '1')

unittest.main()