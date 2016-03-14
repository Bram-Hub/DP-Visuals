import match
import statement


def parse(test_str):
    val = match.match(test_str)
    if val is None:
        return None
    else:
        [kind, matches] = val
        if kind == "lit":
            return statement.Statement(kind, matches)
        elif kind == "~":
            return statement.Statement(kind, parse(matches))
        else:
            return statement.Statement(kind, parse(matches[0]), parse(matches[1]))
