import parse


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
    if stmt_set == []:
        return True
    if False in stmt_set:
        return False

    nxt_lit = findNextSplit(stmt_set)
    nxt_l = parse.parse(nxt_lit)
    nxt_r = parse.parse("~(%s)" % nxt_lit)
    l = []
    r = []
    for stmt in stmt_set:
        stmt_l = stmt.reduce(nxt_l)
        if stmt_l is not True:
            l.append(stmt_l)

        stmt_r = stmt.reduce(nxt_r)
        if stmt_r is not True:
            r.append(stmt_r)

    return satisfiable(l) or satisfiable(r)
