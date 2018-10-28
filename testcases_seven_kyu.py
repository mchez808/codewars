import unittest

from alpha_sequence import alpha_seq


class AlphaSeqTestCase(unittest.TestCase):
    def test_one_letter(self):
        self.assertEqual(alpha_seq('A'),'A')
        self.assertEqual(alpha_seq('a'),'A')


if __name__ == '__main__':
    unittest.main()
