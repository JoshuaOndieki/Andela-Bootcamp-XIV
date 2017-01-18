import unittest
class TestPrimeNumbers(unittest.TestCase):
    def test_input_is_number(self):
        with self.assertRaises(TypeError):
            prime_numbers("String")
    def test_range_is_short(self):
        self.assertEquals(prime_numbers(1,4),3)
    def test_range_is_positive(self):
        self.assertGreater(upperlimit-lower_limit)
    def test_input_is_integer(self):
        self.assertTrue(type(upper_limit)==int and type(lower_limit)==int)
    def test_null_input(self):
        self.assertTrue(len(str(upper_limit))>=1 and len(str(lower_limit))>=1)