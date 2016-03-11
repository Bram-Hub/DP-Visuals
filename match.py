import re

def match(test_str):
    # check against a plain literal
    literalRE = re.compile(ur'^([A-Z])$')
    match = re.search(literalRE, test_str)
    if match:
        return ["literal", match.group(1)]

    # check against a basic negation
    negationRE = re.compile(ur'^~([A-Z])$')
    match = re.search(negationRE, test_str)
    if match:
        return ["negation", match.group(1)]

    # check against a more complex negation
    negationRE = re.compile(ur'^~\(([A-Zv\^~\<\-\>]+)\)$')
    match = re.search(negationRE, test_str)
    if match:
        return ["negation", match.group(1)]

    # check agains a binary connector
    binaryRE = re.compile(ur'^\(([A-Zv\^\-\>\<~]+)\)(v|\^|\-\>|\<\-\>)\(([A-Zv\^\-\>\<~]+)\)$')
    match = re.search(binaryRE, test_str)
    if match:
        if match.group(2) == "v":
            kind = "disjunction"
        elif match.group(2) == "^":
            kind = "conjunction"
        elif match.group(2) == "->":
            kind = "implication"
        elif match.group(2) == "<->":
            kind = "biconditional"
        return [kind, match.group(1, 3)]

    # check agains a binary connector
    binaryRE = re.compile(ur'^\(([A-Zv\^\-\>\<~]+)\)(v|\^|\-\>|\<\-\>)([A-Z]|~[A-Z]|~\([A-Zv\^\-\>\<~]+\))$')
    match = re.search(binaryRE, test_str)
    if match:
        if match.group(2) == "v":
            kind = "disjunction"
        elif match.group(2) == "^":
            kind = "conjunction"
        elif match.group(2) == "->":
            kind = "implication"
        elif match.group(2) == "<->":
            kind = "biconditional"
        return [kind, match.group(1, 3)]

    # check agains a binary connector
    binaryRE = re.compile(ur'^([A-Z]|~[A-Z]|~\([A-Zv\^\-\>\<~]+\))(v|\^|\-\>|\<\-\>)\(([A-Zv\^\-\>\<~]+)\)$')
    match = re.search(binaryRE, test_str)
    if match:
        if match.group(2) == "v":
            kind = "disjunction"
        elif match.group(2) == "^":
            kind = "conjunction"
        elif match.group(2) == "->":
            kind = "implication"
        elif match.group(2) == "<->":
            kind = "biconditional"
        return [kind, match.group(1, 3)]

    # check agains a binary connector   
    binaryRE = re.compile(ur'^([A-Z]|~[A-Z]|~\([A-Zv\^\-\>\<~]+\))(v|\^|\-\>|\<\-\>)([A-Z]|~[A-Z]|~\([A-Zv\^\-\>\<~]+\))$')
    match = re.search(binaryRE, test_str)
    if match:
        if match.group(2) == "v":
            kind = "disjunction"
        elif match.group(2) == "^":
            kind = "conjunction"
        elif match.group(2) == "->":
            kind = "implication"
        elif match.group(2) == "<->":
            kind = "biconditional"
        return [kind, match.group(1, 3)]

    return None


#  \(([A-Zv\^\-\>\<~]+)\)

#  ([A-Z]|~[A-Z]|~\([A-Zv\^\-\>\<~]+\))
