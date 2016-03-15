import sys
import parse
import satisfiable


def open_argument(filename):
    f = open(filename)
    stmt_set = []
    for line in f:
        stmt = parse.parse(line.strip())
        stmt_set.append(stmt)
    conclusion = stmt_set[-1]
    stmt_set = stmt_set[:-1]
    stmt_set.append(parse.parse("~(%s)" % conclusion.__str__()))
    return stmt_set

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Incorrect Usage: python main.py <input file>"
        exit(1)

    stmt_set = open_argument(sys.argv[1])

    if satisfiable.satisfiable(stmt_set):
        print "Satisfiable! Therefore, Invalid Argument!"
    else:
        print "Unsatisfiable! Therefore, Valid Argument!"
