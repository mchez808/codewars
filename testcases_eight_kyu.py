import unittest

from eight_kyu import pillars
from eight_kyu import problem


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


RightMeow = ProblemTestCase()
RightMeow.test_one()
RightMeow.test_str()
