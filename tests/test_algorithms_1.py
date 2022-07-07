import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms import algorithm_1


class TestAlgorithms1(unittest.TestCase):

    def test_search_algorithm1(self):
        alg_impl = algorithm_1.AlgorithmImplementation()
        expected = 21
        actual = alg_impl.add(11)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()