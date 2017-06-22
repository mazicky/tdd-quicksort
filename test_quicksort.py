import unittest

from quicksort import quicksort

class Quicksort(unittest.TestCase):
    def test_length_2(self):
        self.assertEqual(quicksort([1 ,2]), [1, 2])
        self.assertEqual(quicksort([2 ,1]), [1, 2])
        self.assertEqual(quicksort([3, 2 ,1]), [1, 2, 3])
        self.assertEqual(quicksort([5, 6, 3, 2 ,1]), [1, 2, 3, 5, 6])
        self.assertEqual(quicksort([5, 6, 3, 10 , 1, 2]), [1, 2, 3, 5, 6, 10])
