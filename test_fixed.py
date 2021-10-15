import unittest
from fixed import outside_parens, has_all_digits, find_pers_number, countmatch


class TestFixed(unittest.TestCase):
    # Not testing it has been rewritten, just that it still works.
    def test_outside_parens(self):
        self.assertEqual(outside_parens('This is my (short) example.'),
                         'This is my  example.')
        self.assertEqual(outside_parens('(A)B(C)'), 'B')

    def test_has_all_digits(self):
        self.assertTrue(has_all_digits('0123456789'))
        self.assertTrue(has_all_digits('9897060504030201'))
        self.assertFalse(has_all_digits('012345678'))
        self.assertFalse(has_all_digits('987654321'))
        self.assertFalse(has_all_digits('some words'))
        self.assertFalse(has_all_digits('0123234534564568568968908901'))
        self.assertFalse(has_all_digits(100 * '0'))
        self.assertFalse(has_all_digits(''))

    # find_pers_number not tested.

    def test_countmatch(self):
        # These tests work with the original buggy version,
        # so more tests are needed.
        self.assertEqual(countmatch('baboon', 'badger'), 2)
        self.assertEqual(countmatch('crow', 'crocodile'), 3)
        self.assertEqual(countmatch('crow', 'ant'), 0)
        self.assertEqual(countmatch('crowt', 'Crowy'), 4)
        self.assertEqual(countmatch('-crowt', '-Crowy'), 5)
        self.assertEqual(countmatch('bab', 'baboon'), 3)
        self.assertEqual(countmatch('baboon', 'bab'), 3)
        self.assertEqual(countmatch('baboon', ''), 0)
        self.assertEqual(countmatch('', 'baboon'), 0)
        self.assertEqual(countmatch('bnicer', 'bnicer'), 6)
        self.assertEqual(countmatch('baboon', 'baboon'), 6)
        self.assertEqual(countmatch("'baboon's", "'baboon's"), 9)
        self.assertEqual(countmatch("it's", "it's"), 4)


if __name__ == '__main__':
    unittest.main()
