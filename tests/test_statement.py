import unittest
from statement import Statement
from parse import parse


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

    def test_contains(self):
        self.assertEqual(parse("A").contains(), ["A"])
        self.assertEqual(parse("~A").contains(), ["A"])
        self.assertEqual(parse("AvB").contains(), ["A", "B"])
        self.assertEqual(parse("Av(BvC)").contains(), ["A", "B", "C"])
        self.assertEqual(parse("Av((B^C)vD)").contains(), ["A", "B", "C", "D"])


if __name__ == '__main__':
    print "Test Statement:"
    unittest.main()
