import unittest

from big_o import does_name_exist, find_last_name, find_max, get_avg_brand_followers


class TestFindMax(unittest.TestCase):
    def test_various_numners(self):
        nums = [7, 4, 3, 100, 2343243, 343434, 1, 2, 32]
        self.assertEqual(find_max(nums), 2343243)


class TestDoesNameExist(unittest.TestCase):
    def test_various_names(self):
        first_names = ["John", "Jane", "Jack"]
        last_names = ["Doe", "Smith", "Jones"]
        full_name = "JohnDoe"
        self.assertTrue(does_name_exist(first_names, last_names, full_name))


class TestAverageBrandFollowers(unittest.TestCase):
    def test_various_handles(self):
        all_handles = [
            ["cosmofan1010", "cosmogirl", "billjane321"],
            ["cosmokiller", "gr8", "cosmojane3"],
            ["iloveboots", "paperthin"],
        ]
        brand_name = "cosmo"
        self.assertEqual(get_avg_brand_followers(all_handles, brand_name), 1.33)


class TestFindLastName(unittest.TestCase):
    def test_various_names(self):
        names_dict = {"John": "Doe", "Jane": "Smith", "Jack": "Jones"}
        first_name = "John"
        self.assertEqual(find_last_name(names_dict, first_name), "Doe")

    def test_name_not_found(self):
        names_dict = {"John": "Doe", "Jane": "Smith", "Jack": "Jones"}
        first_name = "Bob"
        self.assertIsNone(find_last_name(names_dict, first_name))
