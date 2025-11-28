import unittest

from exponents_grow import (
    decayed_followers,
    get_follower_prediction,
    get_influencer_score,
    num_possible_orders,
)


class TestExponentsGrow(unittest.TestCase):
    def test_get_follower_prediction(self):
        self.assertEqual(get_follower_prediction(100, "fitness", 1), 400)
        self.assertEqual(get_follower_prediction(100, "cosmetic", 1), 300)
        self.assertEqual(get_follower_prediction(100, "other", 1), 200)
        self.assertEqual(get_follower_prediction(100, "fitness", 2), 1600)
        self.assertEqual(get_follower_prediction(100, "cosmetic", 2), 900)
        self.assertEqual(get_follower_prediction(100, "other", 2), 400)
        self.assertEqual(get_follower_prediction(100, "fitness", 3), 6400)
        self.assertEqual(get_follower_prediction(100, "cosmetic", 3), 2700)
        self.assertEqual(get_follower_prediction(100, "other", 3), 800)
        self.assertEqual(get_follower_prediction(100, "fitness", 4), 25600)
        self.assertEqual(get_follower_prediction(100, "cosmetic", 4), 8100)
        self.assertEqual(get_follower_prediction(100, "other", 4), 1600)
        self.assertEqual(get_follower_prediction(100, "fitness", 5), 102400)
        self.assertEqual(get_follower_prediction(100, "cosmetic", 5), 24300)
        self.assertEqual(get_follower_prediction(100, "other", 5), 3200)

    def test_get_influencer_score(self):
        self.assertAlmostEqual(get_influencer_score(40000, 0.3), 5)
        self.assertAlmostEqual(get_influencer_score(43000, 0.1), 2)

    def test_num_possible_orders(self):
        self.assertEqual(num_possible_orders(3), 6)
        self.assertEqual(num_possible_orders(4), 24)
        self.assertEqual(num_possible_orders(5), 120)
        self.assertEqual(num_possible_orders(6), 720)
        self.assertEqual(num_possible_orders(7), 5040)
        self.assertEqual(num_possible_orders(8), 40320)
        self.assertEqual(num_possible_orders(9), 362880)
        self.assertEqual(num_possible_orders(10), 3628800)
        self.assertEqual(
            num_possible_orders(50),
            30414093201713378043612608166064768844377641568960512000000000000,
        )

    def test_decayed_followers(self):
        self.assertEqual(decayed_followers(200, 0.5, 1), 100)
        self.assertEqual(decayed_followers(200, 0.4, 2), 72)
        self.assertEqual(decayed_followers(200, 0.05, 3), 171)
