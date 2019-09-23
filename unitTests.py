
# -*- coding: utf-8 -*-
import unittest

from GithubAPIs import gitData

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGitData(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(gitData(3,4,5),'Right')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()