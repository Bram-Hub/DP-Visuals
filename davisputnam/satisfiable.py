import parse
from ete3 import Tree

# determine the next atom to be split on
def findNextSplit(stmt_set):
    # pick most common atom

    matches = {}
    # for each statement in the set
    for stmt in stmt_set:
        # get the list of atoms from each statement
        contains = stmt.contains()
        # for each atom in the list
        for c in contains:
            # update the count for how many times an atom has been seen
            c_count = matches.get(c, 0)
            matches[c] = c_count + 1

    # return the atom which has occured the most times
    return max(matches.iterkeys(), key=(lambda key: matches[key]))


# the Satisfiable() algorithm
def satisfiable(stmt_set):
    t = Tree()
    t.name = str(stmt_set)

    if stmt_set == []:
        # if the set is empty, the starting set was Satisfiable, OPEN BRANCH
        ob = Tree()
        ob.name = "O"
        t.children.append(ob)
        return True, t
    if False in stmt_set:
        # if there is a False in the set, then something was unsatisfiable, CLOSE BRANCH
        cb = Tree()
        cb.name = "X"
        t.children.append(cb)
        return False, t

    # determine the next atom to split on
    nxt_atm = findNextSplit(stmt_set)

    # get Statements of this atom and its negation
    nxt_l = parse.parse(nxt_atm)
    nxt_r = parse.parse("~(%s)" % nxt_atm)

    # create two new statement sets for the left and right branches
    l = []  # for the statements reduced on the "positive" atom
    r = []  # for the statements reduced on the "negative" atom

    for stmt in stmt_set:
        # reduce the statement on the "positive" atom
        stmt_l = stmt.reduce(nxt_l)
        if stmt_l is not True:
            # don't add it to the new list if the recution was a True
            l.append(stmt_l)

        # reduce the statement on the "negative" atom
        stmt_r = stmt.reduce(nxt_r)
        if stmt_r is not True:
            # don't add it to the new list if the recution was a True
            r.append(stmt_r)

    # return ether the left or right branch
    ret_l, tree_l = satisfiable(l)
    ret_r, tree_r = satisfiable(r)
    t.children.append(tree_l)
    t.children.append(tree_r)
    return ret_l or ret_r, t
