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


    return None
