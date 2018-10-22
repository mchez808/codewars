import unittest

from eight_kyu import invert
from eight_kyu import pillars
from eight_kyu import problem


class InvertTestCase(unittest.TestCase):
    def test_one(self):
        self.assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
        
    def test_two(self):
        self.assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
    
    def test_three(self):
        self.assert_equals(invert([]), [])


class PillarTestCase(unittest.TestCase):
    def test_null(self):
        self.assertEqual(pillars(1, 10, 10), 0)

    def test_2000(self):
        self.assertEqual(pillars(2, 20, 25), 2000)

    def test_high(self):
        self.assertEqual(pillars(11, 15, 30), 15270)


class ProblemTestCase(unittest.TestCase):
    def test_str(self):
        self.assertEqual(problem("hello"), "Error")

    def test_one(self):
        self.assertEqual(problem(1), 56)


# ========
# Test execution
ProblemTestCase.it("Testing ProblemTestCase")
ProblemTestCase.test_one()
ProblemTestCase.test_str()

InvertTestCase.it("Invert values - Basic Tests")
InvertTestCase.test_one()
InvertTestCase.test_two()
InvertTestCase.test_three()
