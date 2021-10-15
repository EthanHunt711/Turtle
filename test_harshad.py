import unittest
from harshad import digit_sum, is_harshad


class TestHarshad(unittest.TestCase):
    def test_digit_sum(self):
        self.assertEqual(digit_sum('123'), 6)
        self.assertEqual(digit_sum('9'), 9)
        self.assertEqual(digit_sum('1003'), 4)
        self.assertEqual(digit_sum('10033'), 7)
        self.assertEqual(digit_sum('123456789'), 45)

    def test_is_harshad(self):
        # low numbers:
        for n in range(1, 11):
            self.assertTrue(is_harshad(n))
        # various examples:
        for n in [12, 20, 30, 42, 63, 90, 117, 198]:
            self.assertTrue(is_harshad(n))
        for n in [11, 17, 43, 99, 118, 182, 199]:
            self.assertFalse(is_harshad(n))


if __name__ == '__main__':
    unittest.main()
