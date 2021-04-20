import unittest

from PaginationHelper import *

collection = range(1,25)

helper = PaginationHelper(collection, 10)

class Test(unittest.TestCase):
  def test_page_count(self):
    self.assertEqual(helper.page_count(), 3)
  def test_page_index(self):
    self.assertEqual(helper.page_index(23), 2)
  def test_item_count(self):
    self.assertEqual(helper.item_count(), 24)