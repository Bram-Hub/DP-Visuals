import unittest
from parse import parse
from satisfiable import findNextSplit, satisfiable


class TestSatisfiable(unittest.TestCase):

    def test_findNextSplit(self):
        test_set = [parse("A")]
        self.assertEqual(findNextSplit(test_set), "A")

        test_set = [parse("AvB")]
        self.assertEqual(findNextSplit(test_set), "A")

        test_set = [parse("AvB"), parse("B")]
        self.assertEqual(findNextSplit(test_set), "B")

    def test_not_satisfiable(self):
        # PLA 1
        stmt_set = [parse("A->(B^C)"), parse("C<->B"), parse("~C"), parse("~(~A)")]
        ret, _ = satisfiable(stmt_set)
        self.assertFalse(ret)

        # PLA 2
        stmt_set = [parse("K->H"), parse("H->L"), parse("L->M"), parse("~(K->M)")]
        ret, _ = satisfiable(stmt_set)
        self.assertFalse(ret)

        # PLA 7
        stmt_set = [parse("((CvD)^H)->A"), parse("D"), parse("~(H->A)")]
        ret, _ = satisfiable(stmt_set)
        self.assertFalse(ret)

    def test_satisfiable(self):
        # PLA 4
        stmt_set = [parse("A^(BvC)"), parse("(~CvH)->(H->~H)"), parse("~(A^B)")]
        ret, _ = satisfiable(stmt_set)
        self.assertTrue(ret)

        # PLA 12
        stmt_set = [parse("(~JvK)->(L^M)"), parse("~(~JvK)"), parse("~(~(L^M))")]
        ret, _ = satisfiable(stmt_set)
        self.assertTrue(ret)

if __name__ == '__main__':
    print "Test satisfiable():"
    unittest.main()
