import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms import search_algorithms


class TestAlgorithms1(unittest.TestCase):

    def test_linear_search_method(self):
        alg_impl = search_algorithms.AlgorithmImplementation()
        test_cases = [{'sequence':[1,5,6,9,21,45], 'query':6 , 'expected':2},{'sequence':[2,5,6,7,7,8,8,10], 'query':8 , 'expected':5},{'sequence':[], 'query':11 , 'expected':-1},{'sequence':[3,4,8,23,41], 'query':6 , 'expected':-1}]
        for test_case in test_cases:
            actual = alg_impl.linear_search(**test_case)
            self.assertEqual(actual, test_case['expected'],msg='failed test case: input sequence = {}, query = {}, expected output = {}, actual returned output = {}'.format(test_case['sequence'], test_case['query'], test_case['expected'], actual))


if __name__ == '__main__':
    unittest.main()