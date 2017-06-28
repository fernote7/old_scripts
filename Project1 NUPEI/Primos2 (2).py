__author__ = 'fernando.ormonde'

import unittest

class primostest(unittest.TestCase):

    def test_retorna_1_ao_receber_1(self):
        self.assertEqual(primos(1), [1])
    def test_retorna_2_ao_receber_2(self):
        self.assertEqual(primos(2), [1, 2])
    def test_retorna_3_ao_receber_3(self):
        self.assertEqual(primos(3), [1, 2, 3])


unittest.main()