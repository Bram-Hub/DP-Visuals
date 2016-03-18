import match
import statement


# recursively parse a statement from a string
def parse(test_str):
    # match the string to its main connector
    val = match.match(test_str)
    if val is None:
        return None
    else:
        # split the result into a connector type and the internal matches
        [kind, matches] = val
        # construct a statement (recursively) based on the connector type
        if kind == "lit":
            return statement.Statement(kind, matches)
        elif kind == "~":
            return statement.Statement(kind, parse(matches))
        else:
            return statement.Statement(kind, parse(matches[0]), parse(matches[1]))
