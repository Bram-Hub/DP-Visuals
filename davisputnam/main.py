import sys
import parse
import statement
import satisfiable

from ete3 import Tree, TreeStyle, TextFace


# read an argument from a file and return a set of the statements contained within
def open_argument(filename):
    try:
        f = open(filename)  # open the file
    except:
        print "Could not open file: %s" % filename
        exit(1)

    stmt_set = []
    for line in f:
        line = line.strip().replace(" ", "")  # strip all of the whitespace
        stmt = parse.parse(line)  # parse the line to get a statement

        # make sure that the line was properly parsed
        if stmt is None:
            print "Parsing Error: %s" % line
            exit(1)

        stmt_set.append(stmt)  # add the statement to the set

    # take the last statement out of the set, and negate it
    conclusion = stmt_set[-1]
    neg = statement.Statement("~", conclusion)
    stmt_set = stmt_set[:-1]

    # re-add the negated conclusion to the set
    stmt_set.append(neg)

    # return the set
    return stmt_set

if __name__ == "__main__":
    # ensure proper usage
    if len(sys.argv) != 3:
        print "Incorrect Usage: python main.py <input file> <output file>"
        exit(1)

    # get a statement set from the given file
    stmt_set = open_argument(sys.argv[1])

    # call the Satisfiable() algorithm to determine whether or not the argument is valid
    sat, tree = satisfiable.satisfiable(stmt_set)
    print tree.get_ascii(show_internal=True)

    ts = TreeStyle()
    ts.show_leaf_name = False

    for child in tree.traverse():
        child.add_face(TextFace(child.name), column=0, position="branch-top")

    tree.render(sys.argv[2], w=2000, tree_style=ts)

    if sat:
        print "Satisfiable! Therefore, Invalid Argument!"
    else:
        print "Unsatisfiable! Therefore, Valid Argument!"
