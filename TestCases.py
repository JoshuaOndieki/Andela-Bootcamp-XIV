import unittest
class TestPrimeNumbers(unittest.TestCase):
    def test_produce_prime_numbers(self):
        primes = [3, 5]
        prime = prime_numbers(1, 6)
        self.assertListEqual(primes, prime,msg="Range of 1-6 should return [3,5] as the prime numbers")
    def test_return_not_nonetype(self):
        self.assertFalse(prime_numbers(1,6)==[],msg="Range 1-6 should not return empty list")
    def test_input_is_number(self):
        with self.assertRaises(TypeError,msg="Should raise type error if a string is passed as argument"):
            prime_numbers("String")
    def test_return_value_is_list(self):
        self.assertTrue(isinstance(prime_numbers(1,10),list),msg="The function should return a list")
    def test_valueerror(self):
        self.assertRaises(ValueError,msg="Should raise type error if a string is passed")