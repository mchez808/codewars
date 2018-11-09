import unittest

from seven_kyu import alpha_seq, reverse_alternate


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


class reverseAlternateTestCase(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(reverse_alternate("Did it work?"), "Did ti work?")
        self.assertEqual(reverse_alternate("I really hope it works this time..."), "I yllaer hope ti works siht time...")
        self.assertEqual(reverse_alternate("Reverse this string, please!"), "Reverse siht string, !esaelp")
        self.assertEqual(reverse_alternate("Have a beer"), "Have a beer")
        self.assertEqual(reverse_alternate(""), "")


if __name__ == '__main__':
    unittest.main()
    reverseAlternateTestCase()
