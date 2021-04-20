import unittest

from .listUtils import *

class Test(unittest.TestCase):
  def test_page_count(self):
    Test.assert_equals(list([1,2,3,4,5]).over(4), [5], "Nope")
