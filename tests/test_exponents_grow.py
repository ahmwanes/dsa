import unittest

from exponents_grow import (
    decayed_followers,
    get_follower_prediction,
    get_influencer_score,
    log_scale,
    num_possible_orders,
)


class TestGetFollowerPrediction(unittest.TestCase):
    def test_various_categories_and_years(self):
        """get_follower_prediction should grow followers by category-specific factors."""
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


class TestGetInfluencerScore(unittest.TestCase):
    def test_scores_for_given_followers_and_engagement(self):
        """get_influencer_score returns expected bucketed scores (use approximate equality)."""
        self.assertAlmostEqual(get_influencer_score(40000, 0.3), 5)
        self.assertAlmostEqual(get_influencer_score(43000, 0.1), 2)


class TestNumPossibleOrders(unittest.TestCase):
    def test_factorial_values(self):
        """num_possible_orders should compute factorial for small integers and large ones."""
        self.assertEqual(num_possible_orders(3), 6)
        self.assertEqual(num_possible_orders(4), 24)
        self.assertEqual(num_possible_orders(5), 120)
        self.assertEqual(num_possible_orders(6), 720)
        self.assertEqual(num_possible_orders(7), 5040)
        self.assertEqual(num_possible_orders(8), 40320)
        self.assertEqual(num_possible_orders(9), 362880)
        self.assertEqual(num_possible_orders(10), 3628800)

    def test_very_large_factorial(self):
        """Large factorial (n=50) should match the known exact value."""
        self.assertEqual(
            num_possible_orders(50),
            30414093201713378043612608166064768844377641568960512000000000000,
        )


class TestDecayedFollowers(unittest.TestCase):
    def test_decay_over_time(self):
        """decayed_followers should apply decay factor over n periods correctly."""
        self.assertEqual(decayed_followers(200, 0.5, 1), 100)
        self.assertEqual(decayed_followers(200, 0.4, 2), 72)
        self.assertEqual(decayed_followers(200, 0.05, 3), 171)


class TestLogScale(unittest.TestCase):
    def test_douple_digits(self):
        """log_scale should return the logarithm of a number."""
        data = [1, 10, 100, 1000]
        base = 10
        expected = [0.0, 1.0, 2.0, 3.0]
        self.assertEqual(log_scale(data, base), expected)

    def test_single_digits(self):
        """log_scale should return the logarithm of a number."""
        data = [1, 2, 4, 8]
        base = 2
        expected = [0.0, 1.0, 2.0, 3.0]
        self.assertEqual(log_scale(data, base), expected)
