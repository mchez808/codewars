import unittest

from alpha_sequence import alpha_seq

inputs = ("alpha_seq('A')",)
outputs = ("A",)
# inputs = ("alpha_seq('A')", "alpha_seq('a')")
# outputs = ("A", "A")
dict_testcase = {"input":inputs, "output":outputs}


class AlphaSeqTestCase(unittest.TestCase):
    def test_one_letter(self):
        # self.assertEqual(alpha_seq('A'),'A')
        # self.assertEqual(alpha_seq('a'),'A')
        # self.assertEqual(eval(tc1["input"]),tc1["output"])
        # self.assertEqual(eval(tc2["input"]),tc2["output"])
        self.assertEqual(eval(


if __name__ == '__main__':
    unittest.main()
