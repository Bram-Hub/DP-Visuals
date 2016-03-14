import unittest
from statement import Statement


class TestStatement(unittest.TestCase):

    def test_lit(self):
        self.assertEqual(Statement("lit", "A").__str__(), "A")

    def test_negation(self):
        self.assertEqual(Statement("~", "A").__str__(), "~(A)")
        self.assertEqual(Statement("~", "v(A, B)").__str__(), "~(v(A, B))")

    def test_disjunction(self):
        self.assertEqual(Statement("v", "A", "B").__str__(), "v(A, B)")

    def test_conjunction(self):
        self.assertEqual(Statement("^", "A", "B").__str__(), "^(A, B)")

    def test_implication(self):
        self.assertEqual(Statement("->", "A", "B").__str__(), "->(A, B)")

    def test_biconditional(self):
        self.assertEqual(Statement("<->", "A", "B").__str__(), "<->(A, B)")


if __name__ == '__main__':
    print "Test Statement:"
    unittest.main()
