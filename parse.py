from match import match
from statement import Statement

def parse(test_str):
    val = match(test_str)
    if val is None:
        return None
    else:
        [kind, matches] = val
        if kind == "lit":
            return Statement(kind, matches)
        elif kind == "~":
            return Statement(kind, parse(matches))
        else:
            return Statement(kind, parse(matches[0]), parse(matches[1]))
