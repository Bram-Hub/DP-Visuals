import unittest
from parse import parse
from satisfiable import findNextSplit


class TestSatisfiable(unittest.TestCase):

    def test_findNextSplit(self):
        test_set = [parse("A")]
        self.assertEqual(findNextSplit(test_set), "A")

        test_set = [parse("AvB")]
        self.assertEqual(findNextSplit(test_set), "A")

        test_set = [parse("AvB"), parse("B")]
        self.assertEqual(findNextSplit(test_set), "B")

if __name__ == '__main__':
    print "Test satisfiable():"
    unittest.main()
