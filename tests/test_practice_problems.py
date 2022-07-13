import os
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from algorithms import practice_problems


class TestProblems(unittest.TestCase):
    def test_rotated_sorted_list(self):
        pp = practice_problems.PracticeProblems()
        test_cases = [{'sequence':[9, 11,14, 17,1,4,5,7],'output':4},{'sequence':[21,8,12,15],'output':1}, {'sequence':[3,6,8,9,11,13],'output':0},{'sequence':[45,65,3,23,32,36],'output':2}]
        for test_case in test_cases:
           actual = pp.rotated_sorted_list(test_case['sequence'])
           self.assertEqual(test_case['output'], actual, msg='sequence: {}, expected output: {}, actual output: {}'.format(test_case['sequence'],test_case['output'],actual))
           
if __name__ == '__main__':
    unittest.main() ౪౫ీ