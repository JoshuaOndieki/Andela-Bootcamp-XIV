import unittest
from HttpWebGetRequest import *

class testing_get_data(unittest.TestCase):
    def test_value_error(self):
        with self.assertRaises(ValueError):
            get_data("")