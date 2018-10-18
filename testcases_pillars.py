import unittest

from eight_kyu import pillars


class PillarTestCase(unittest.TestCase):
    def test_null(self):
        self.assertEqual(pillars(1, 10, 10), 0)

    def test_2000(self):
        self.assertEqual(pillars(2, 20, 25), 2000)

    def test_high(self):
        self.assertEqual(pillars(11, 15, 30), 15270)

RightMeow = PillarTestCase()
RightMeow.test_null()
RightMeow.test_2000()
RightMeow.test_high()

# Test.describe("Basic Tests")
# Test.assert_equals(pillars(1, 10, 10) , 0)
# Test.assert_equals(pillars(2, 20, 25) , 2000)
# Test.assert_equals(pillars(11, 15, 30) , 15270)