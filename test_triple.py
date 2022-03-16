import unittest

from triple import MyTriple


class TripleTestCase(unittest.TestCase):

    def test_triple_creation(self):
        tr = MyTriple(1,2,3)
        self.assertTrue(True)

    def test_iterate_triple(self):
        results = [1, 2, 3]
        tr = MyTriple(1, 2, 3)

        index = 0
        for el in tr:
            self.assertEquals(el, results[index])
            index += 1


if __name__ == '__main__':
    unittest.main()