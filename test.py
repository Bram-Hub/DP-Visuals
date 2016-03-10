import re
p = re.compile(ur'^([A-Z]|~[A-Z]|\([A-Zv\^~]+\)|~\([A-Zv\^~]+\))(v|\^|->|<->)([A-Z]|~[A-Z]|\([A-Zv\^~]+\)|~\([A-Zv\^~]+\))$')
test_str = u"(A^B)->(CvD)"

match = re.search(p, test_str)

if match:
    print match.group(0), match.group(1), match.group(2), match.group(3)
else:
    print "no match"
