import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms import practice_problems


class TestProblems(unittest.TestCase):
    def test_rotated_sorted_list(self):
        pp = practice_problems.PracticeProblems()
        test_cases = [{'sequence':[9, 11,14, 17,1,4,5,7],'output':4},{'sequence':[21,8,12,15],'output':1}]
        for test_case in test_cases:
           actual = rotated_sorted_list(test_case['sequence'])
           self.assertEqual(test_case['output'], actual)
           
if __name__ == '__main__':
    unittest.main()