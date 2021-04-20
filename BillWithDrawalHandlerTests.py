import unittest
from .BillWithDrawalHandler import withdraw

class Test(unittest.TestCase):
    def test_should_handle_basic_tests(self):
        self.assertEqual(withdraw(40), [0, 0, 2])
        self.assertEqual(withdraw(250), [2, 1, 0])
        self.assertEqual(withdraw(260), [2, 0, 3])
        self.assertEqual(withdraw(230), [1, 1, 4])
        self.assertEqual(withdraw(60), [0, 0, 3])