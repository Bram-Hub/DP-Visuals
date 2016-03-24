import unittest
from parse import parse


class TestParsing(unittest.TestCase):

    def test_no_match(self):
        vals = []
        vals.append(parse("a"))
        vals.append(parse("AB"))
        vals.append(parse("A B"))

        for val in vals:
            self.assertIsNone(val, msg="Invalid pattern Parsed!")

    def test_literal(self):
        statement = parse("A")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "lit")

    def test_negation(self):
        statement = parse("~A")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "~")
        self.assertEqual(statement.value1().type, "lit")

        statement = parse("~(A)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "~")
        self.assertEqual(statement.value1().type, "lit")

    def test_disjunction(self):
        statement = parse("AvB")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "v")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "(AvB)")

        statement = parse("Av(BvC)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "v")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "v")
        self.assertEqual(statement.__str__(), "(Av(BvC))")

        statement = parse("(AvB)vC")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "v")
        self.assertEqual(statement.value1().type, "v")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "((AvB)vC)")

        statement = parse("(AvB)v(CvD)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "v")
        self.assertEqual(statement.value1().type, "v")
        self.assertEqual(statement.value2().type, "v")
        self.assertEqual(statement.__str__(), "((AvB)v(CvD))")

        statement = parse("Av(Bv(CvD))")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.__str__(), "(Av(Bv(CvD)))")

    def test_conjunction(self):
        statement = parse("A^B")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "^")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "(A^B)")

        statement = parse("A^(B^C)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "^")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "^")
        self.assertEqual(statement.__str__(), "(A^(B^C))")

        statement = parse("(A^B)^C")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "^")
        self.assertEqual(statement.value1().type, "^")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "((A^B)^C)")

        statement = parse("(A^B)^(C^D)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "^")
        self.assertEqual(statement.value1().type, "^")
        self.assertEqual(statement.value2().type, "^")
        self.assertEqual(statement.__str__(), "((A^B)^(C^D))")

        statement = parse("A^(B^(C^D))")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.__str__(), "(A^(B^(C^D)))")

    def test_implication(self):
        statement = parse("A->B")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "->")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "(A->B)")

        statement = parse("A->(B->C)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "->")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "->")
        self.assertEqual(statement.__str__(), "(A->(B->C))")

        statement = parse("(A->B)->C")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "->")
        self.assertEqual(statement.value1().type, "->")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "((A->B)->C)")

        statement = parse("(A->B)->(C->D)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "->")
        self.assertEqual(statement.value1().type, "->")
        self.assertEqual(statement.value2().type, "->")
        self.assertEqual(statement.__str__(), "((A->B)->(C->D))")

        statement = parse("A->(B->(C->D))")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.__str__(), "(A->(B->(C->D)))")

    def test_biconditional(self):
        statement = parse("A<->B")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "<->")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "(A<->B)")

        statement = parse("A<->(B<->C)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "<->")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "<->")
        self.assertEqual(statement.__str__(), "(A<->(B<->C))")

        statement = parse("(A<->B)<->C")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "<->")
        self.assertEqual(statement.value1().type, "<->")
        self.assertEqual(statement.value2().type, "lit")
        self.assertEqual(statement.__str__(), "((A<->B)<->C)")

        statement = parse("(A<->B)<->(C<->D)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "<->")
        self.assertEqual(statement.value1().type, "<->")
        self.assertEqual(statement.value2().type, "<->")
        self.assertEqual(statement.__str__(), "((A<->B)<->(C<->D))")

        statement = parse("A<->(B<->(C<->D))")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.__str__(), "(A<->(B<->(C<->D)))")

    def test_mixed(self):
        statement = parse("Av(B^C)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "v")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "^")

        statement = parse("A->(B<->C)")
        self.assertIsNotNone(statement)
        self.assertEqual(statement.type, "->")
        self.assertEqual(statement.value1().type, "lit")
        self.assertEqual(statement.value2().type, "<->")

if __name__ == '__main__':
    print "Test parse():"
    unittest.main()
