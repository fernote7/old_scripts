__author__ = 'fernando.ormonde'


def maxsum(bets):
    maximum = None
    for i in range(len(bets)):
        for j in range(i, len(bets)):
            maximum = max(maximum, sum(bets[i:j+1]))

    return maximum

print maxsum([20, -10, 3])



#testes

import unittest

class TestMaxSum(unittest.TestCase):
    def test_one_bet(self):
        self.assertEqual(maxsum([42]), 42)
        self.assertEqual(maxsum([20]), 20)

    def test_all_won_bets(self):
        self.assertEqual(maxsum([1, 2]), 3)
        self.assertEqual(maxsum([10, 20]), 30)
        self.assertEqual(maxsum([10, 20, 30, 40]), 100)

    def test_a_won_bet_and_lost_bet(self):
        self.assertEqual(maxsum([-7, 5]), 5)


    def test_two_won_bet_and_lost_bet(self):
        self.assertEqual(maxsum([-7, 12, 5]), 17)

    def test_two_won_bet_and_lost_betneg(self):
        self.assertEqual(maxsum([-7, -12, -5]), -5)

unittest.main()