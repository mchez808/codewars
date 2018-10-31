import unittest

from seven_kyu import alpha_seq


class AlphaSeqTestCase(unittest.TestCase):
    def test_one_letter(self):
        self.assertEqual(alpha_seq('A'),
                         'A')
        self.assertEqual(alpha_seq('a'),
                         'A')
        self.assertEqual(alpha_seq('B'),
                         'Bb')
        self.assertEqual(alpha_seq('bb'),
                         'Bb,Bb')
        self.assertEqual(alpha_seq('Cbc'),
                         'Bb,Ccc,Ccc')
        self.assertEqual(alpha_seq('ZpglnRqenU'),
                         'Eeeee,Ggggggg,Llllllllllll,Nnnnnnnnnnnnnn,Nnnnnnnnnnnnnn,Pppppppppppppppp,Qqqqqqqqqqqqqqqqq,Rrrrrrrrrrrrrrrrrr,Uuuuuuuuuuuuuuuuuuuuu,Zzzzzzzzzzzzzzzzzzzzzzzzzz'
                        )


if __name__ == '__main__':
    unittest.main()
