import unittest

from quicksort import quicksort

class Quicksort(unittest.TestCase):
    def test_length_2(self):
        self.assertEqual(quicksort([1 ,2]), [1, 2])

