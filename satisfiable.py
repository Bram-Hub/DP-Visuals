def findNextSplit(stmt_set):
    # pick most common literal
    matches = {}
    for stmt in stmt_set:
        contains = stmt.contains()
        for c in contains:
            c_count = matches.get(c, 0)
            matches[c] = c_count + 1

    return max(matches.iterkeys(), key=(lambda key: matches[key]))

def satisfiable(stmt_set):
    return False
