import unittest
from strings import (indef, parens, three_rays, swap,
                     firstdigit, numbers_for_uc, grid)


class TestStrings(unittest.TestCase):
    def test_indef(self):
        self.assertEqual(indef('cat'), 'a cat')
        self.assertEqual(indef('octopus'), 'an octopus'),
        self.assertEqual(indef('orange ball'), 'an orange ball')

    def test_parens(self):
        self.assertEqual(parens('abc def'), '(a)(b)(c)( )(d)(e)(f)')
        self.assertEqual(parens('0'), '(0)')

    def test_parens_empty(self):
        self.assertEqual(parens(''), '')

    # def test_three_rays(self):
    # Testing functions that should print stuff is harder.

    def test_swap(self):
        self.assertEqual(swap('python'), 'honpyt')
        self.assertEqual(swap('casebook'), 'bookcase')
        self.assertEqual(swap('oddlength'), 'oddlength')
        self.assertEqual(swap(''), '')

    def test_firstdigit(self):
        self.assertEqual(firstdigit('Bla bla 5th Street'), 5)
        self.assertEqual(firstdigit('103'), 1)
        self.assertEqual(firstdigit('no digit'), 0)
        self.assertEqual(firstdigit(''), 0)

    def test_numbers_for_uc(self):
        self.assertEqual(numbers_for_uc('small'), 'small')
        self.assertEqual(numbers_for_uc('BIG!'), '[0][1][2]!')
        self.assertEqual(numbers_for_uc('McDonald and IBM'),
                         '[0]c[2]onald and [13][14][15]')
        self.assertEqual(numbers_for_uc(''), '')

    # grid not tested


if __name__ == '__main__':
    unittest.main()
