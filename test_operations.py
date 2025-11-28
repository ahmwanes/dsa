import unittest

from operations import find_maximum, find_minimun


class TestFindMinimum(unittest.TestCase):
    def test_normal_list(self):
        """Typical list with minimum in the middle."""
        nums = [3, 1, 4, 1, 5, 9]
        self.assertEqual(find_minimun(nums), 1)

    def test_negative_and_positive(self):
        """Mixture of negative and positive integers."""
        nums = [10, -2, 0, 7, -5]
        self.assertEqual(find_minimun(nums), -5)

    def test_single_element(self):
        """Single-element list should return that element."""
        nums = [42]
        self.assertEqual(find_minimun(nums), 42)

    def test_duplicates(self):
        """All identical elements should return that identical value."""
        nums = [2, 2, 2, 2]
        self.assertEqual(find_minimun(nums), 2)

    def test_floats_and_precision(self):
        """List with floats and negative values; use almost equal for safety."""
        nums = [3.5, 2.1, 2.1001, -1.2000001]
        self.assertAlmostEqual(find_minimun(nums), -1.2000001)

    def test_large_numbers(self):
        """Works with large magnitude numbers."""
        nums = [10**6, 10**9, -(10**12), 123]
        self.assertEqual(find_minimun(nums), -(10**12))

    def test_empty_list_raises(self):
        """Empty input list must raise ValueError."""
        with self.assertRaises(ValueError):
            find_minimun([])


class TestFindMaximun(unittest.TestCase):
    def test_normal_list(self):
        """Typical list with minimum in the middle."""
        nums = [3, 1, 4, 1, 5, 9]
        self.assertEqual(find_maximum(nums), 9)

    def test_negative_and_positive(self):
        """Mixture of negative and positive integers."""
        nums = [10, -2, 0, 7, -5]
        self.assertEqual(find_maximum(nums), 10)

    def test_single_element(self):
        """Single-element list should return that element."""
        nums = [42]
        self.assertEqual(find_maximum(nums), 42)

    def test_duplicates(self):
        """All identical elements should return that identical value."""
        nums = [2, 2, 2, 2]
        self.assertEqual(find_maximum(nums), 2)

    def test_floats_and_precision(self):
        """List with floats and negative values; use almost equal for safety."""
        nums = [3.5, 2.1, 2.1001, -1.2000001]
        self.assertAlmostEqual(find_maximum(nums), 3.5)

    def test_large_numbers(self):
        """Works with large magnitude numbers."""
        nums = [10**6, 10**9, -(10**12), 123]
        self.assertEqual(find_maximum(nums), 10**9)

    def test_empty_list_raises(self):
        """Empty input list must raise ValueError."""
        with self.assertRaises(ValueError):
            find_minimun([])


if __name__ == "__main__":
    unittest.main()
