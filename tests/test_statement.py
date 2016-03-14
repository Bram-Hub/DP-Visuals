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

    def test_eqality(self):
        self.assertEqual(parse("A"), parse("A"))
        self.assertNotEqual(parse("A"), parse("B"))

        self.assertEqual(parse("AvB"), parse("AvB"))
        self.assertEqual(parse("Av(B->C)"), parse("Av(B->C)"))

    def test_reduce_literal(self):
        stmt = parse("A")
        red = parse("A")
        self.assertTrue(stmt.reduce(red))

        stmt = parse("A")
        red = parse("~A")
        self.assertFalse(stmt.reduce(red))

    def test_reduce_negation(self):
        stmt = parse("A")
        red = parse("B")
        self.assertEqual(stmt.reduce(red), stmt)

        stmt = parse("~(~A)")
        red = parse("A")
        self.assertTrue(stmt.reduce(red))

        stmt = parse("~(AvB)")
        red = parse("~B")
        self.assertEqual(stmt.reduce(red), parse("~A"))

    def test_reduce_disjunction(self):
        stmt = parse("AvB")
        red = parse("~A")
        self.assertEqual(stmt.reduce(red), parse("B"))

        stmt = parse("AvB")
        red = parse("A")
        self.assertTrue(stmt.reduce(red))

        stmt = parse("AvB")
        red = parse("~B")
        self.assertEqual(stmt.reduce(red), parse("A"))

        stmt = parse("AvB")
        red = parse("C")
        self.assertEqual(stmt.reduce(red), parse("AvB"))

    def test_reduce_conjunction(self):
        stmt = parse("A^B")
        red = parse("~A")
        self.assertFalse(stmt.reduce(red))

        stmt = parse("A^B")
        red = parse("A")
        self.assertEqual(stmt.reduce(red), parse("B"))

        stmt = parse("A^B")
        red = parse("~B")
        self.assertFalse(stmt.reduce(red))

        stmt = parse("A^B")
        red = parse("C")
        self.assertEqual(stmt.reduce(red), parse("A^B"))

    def test_reduce_implication(self):
        stmt = parse("A->B")
        red = parse("A")
        self.assertEqual(stmt.reduce(red), parse("B"))

        stmt = parse("A->B")
        red = parse("~A")
        self.assertTrue(stmt.reduce(red))

        stmt = parse("A->B")
        red = parse("B")
        self.assertTrue(stmt.reduce(red))

        stmt = parse("A->B")
        red = parse("~B")
        self.assertEqual(stmt.reduce(red), parse("~A"))

        stmt = parse("A->B")
        red = parse("C")
        self.assertEqual(stmt.reduce(red), parse("A->B"))

    def test_reduce_biconditional(self):
        stmt = parse("A<->B")
        red = parse("A")
        self.assertEqual(stmt.reduce(red), parse("B"))

        stmt = parse("A<->B")
        red = parse("~A")
        self.assertEqual(stmt.reduce(red), parse("~B"))

        stmt = parse("A<->B")
        red = parse("B")
        self.assertEqual(stmt.reduce(red), parse("A"))

        stmt = parse("A<->B")
        red = parse("~B")
        self.assertEqual(stmt.reduce(red), parse("~A"))

        stmt = parse("A<->B")
        red = parse("C")
        self.assertEqual(stmt.reduce(red), parse("A<->B"))


if __name__ == '__main__':
    print "Test Statement:"
    unittest.main()
