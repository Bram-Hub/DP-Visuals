import unittest
from match import match

class TestMatching(unittest.TestCase):

  def test_literal(self):
      val = match("A")
      self.assertIsNotNone(val)
      [kind, matches] = val
      self.assertEqual(kind, "literal")
      self.assertEqual(matches, "A")

  def test_negation(self):
    # define the test cases
    cases = {
      "~A":"A",
      "~(AvB)": "AvB",
      "~(A^B)": "A^B",
      "~(A->B)": "A->B",
      "~(A<->B)": "A<->B",
      "~(~A^~B)": "~A^~B",
    }

    for case in cases:
      val = match(case)
      self.assertIsNotNone(val, msg="match(%s) == None" % case)
      [kind, matches] = val
      self.assertEqual(kind, "negation")
      self.assertEqual(matches, cases[case])


  def test_no_match(self):
      vals = []
      vals.append(match("a"))
      vals.append(match("AB"))
      vals.append(match("A B"))

      for val in vals:
        self.assertIsNone(val)



if __name__ == '__main__':
    unittest.main()
