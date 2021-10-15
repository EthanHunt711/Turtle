import unittest
from week5 import mymin, find_longer, first_longer
from week5 import allit, anti_allit, addpairs, endings
from week5 import procrustean, midchars

# no tests for these:
# progress, histogram, vhistogram


class TestWeek5(unittest.TestCase):
    def test_mymin(self):
        # test with the minimum being first, last and somewhere inbetween
        self.assertEqual(mymin([2, 10, 9, 8, 7]), 2)
        self.assertEqual(mymin([10, 2, 9, 8, 7]), 2)
        self.assertEqual(mymin([10, 9, 8, 7, 2]), 2)
        # shortest possible list
        self.assertEqual(mymin([20]), 20)

    def test_find_longer(self):
        words = ['nitwit', 'blubber', 'oddment', 'tweak']
        self.assertEqual(find_longer(words, 0), words)
        self.assertEqual(find_longer(words, 1), words)
        self.assertEqual(find_longer(words, 3), words)
        self.assertEqual(find_longer(words, 4), words)
        self.assertEqual(find_longer(words, 5),
                         ['nitwit', 'blubber', 'oddment'])
        self.assertEqual(find_longer(words, 6), ['blubber', 'oddment'])
        self.assertEqual(find_longer(words, 7), [])

    def test_first_longer(self):
        words = ['nitwit', 'blubber', 'oddment', 'tweak']
        self.assertEqual(first_longer(words, 0), 'nitwit')
        self.assertEqual(first_longer(words, 5), 'nitwit')
        self.assertEqual(first_longer(words, 6), 'blubber')
        self.assertEqual(first_longer(words, 7), None)
        words = ['a', 'b', 'c', 'this', 'd', 'e']
        self.assertEqual(first_longer(words, 0), 'a')
        self.assertEqual(first_longer(words, 1), 'this')
        self.assertEqual(first_longer(words, 3), 'this')
        self.assertEqual(first_longer(words, 4), None)

    def test_allit_basic(self):
        self.assertTrue(allit(['per', 'prefers', 'python']))
        self.assertFalse(allit(['per', 'likes', 'lisp']))
        self.assertFalse(allit(['per', 'prefers', 'lisp']))
        self.assertFalse(allit(['who', 'prefers', 'python?']))

    def test_allit_case(self):
        self.assertTrue(allit(['Per', 'prefers', 'python']))
        self.assertTrue(allit(['Per', 'prefers', 'Python']))
        self.assertTrue(allit(['per', 'Prefers', 'python']))

    def test_allit_singleton(self):
        self.assertTrue(allit(['Turing']))

    def test_allit_empty(self):
        self.assertTrue(allit([]))

    def test_anti_allit_true(self):
        words = ['ape', 'bat', 'cat', 'dog', 'eagle']
        self.assertTrue(anti_allit(words))
        self.assertTrue(anti_allit(words[1:]))
        self.assertTrue(anti_allit(words[2:]))

    def test_anti_allit_false(self):
        self.assertFalse(anti_allit(['ape', 'ape', 'bat', 'cat', 'dog', 'ee']))
        self.assertFalse(anti_allit(['ape', 'bat', 'ape', 'cat', 'dog', 'ee']))
        self.assertFalse(anti_allit(['ape', 'bat', 'cat', 'ape', 'dog', 'ee']))
        self.assertFalse(anti_allit(['ape', 'bat', 'cat', 'dog', 'ape', 'ee']))
        self.assertFalse(anti_allit(['ape', 'bat', 'cat', 'dog', 'ee', 'ape']))
        self.assertFalse(anti_allit(['ape', 'bat', 'cat', 'cat', 'dog', 'ee']))
        self.assertFalse(anti_allit(['ape', 'bat', 'cat', 'dog', 'cat', 'ee']))

    def test_anti_allit_singleton(self):
        self.assertTrue(anti_allit(['wolf']))

    # "All" the 0 words have different letters, but assignment didn't mention
    # the empty list explicitly. Don't complain if solutions for some reason
    # do it elseway.
    # def test_anti_allit_empty(self):
    #     self.assertTrue(anti_allit([]))

    # don't bother testing with case differences for anti_allit

    def test_addpairs(self):
        # Example in the assignment
        self.assertEqual(addpairs([10, 100, 1000, 2]),
                         [110, 1010, 12, 1100, 102, 1002])
        #self.assertEqual(addpairs([1, 1, 10]),
         #                [2, 11, 11])
        # Test very short lists as well, where there are no two numbers to add
        self.assertEqual(addpairs([313]), [])
        self.assertEqual(addpairs([]), [])

    def test_endings(self):
        # Example in the assignment
        self.assertEqual(endings('Turing'),
                         ['Turing', 'uring', 'ring', 'ing', 'ng', 'g'])
        self.assertEqual(endings(''), [])

    def test_procrustean(self):
        ns = [100, 10, 25, 1, 2000, 313, 99]
        procrustean(ns, 20, 300)
        self.assertEqual(ns, [100, 20, 25, 20, 300, 300, 99])
        # Also test where all numbers are too small
        ns = [100, 10, 25, 1, 2000, 313, 99]
        procrustean(ns, 3000, 4000)
        self.assertEqual(ns, [3000, 3000, 3000, 3000, 3000, 3000, 3000])
        # Here almost all numbers are too large
        ns = [100, 10, 25, 1, 2000, 313, 99]
        procrustean(ns, 0, 10)
        self.assertEqual(ns, [10, 10, 10, 1, 10, 10, 10])

    def test_midchars(self):
        self.assertEqual(midchars(['ant', 'gnu', 'giraffe', 'fox']), 'inor')
        self.assertEqual(midchars(['aa', 'bb']), '')
        self.assertEqual(midchars(['aa', 'bob']), 'o')
        self.assertEqual(midchars(['abaz', 'bob', 'xyzza']), 'oy')
        self.assertEqual(midchars(['xyzza', 'abaz', 'bob']), 'oy')
        self.assertEqual(midchars([]), '')


if __name__ == '__main__':
    unittest.main()
