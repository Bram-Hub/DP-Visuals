import sys
import parse

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Incorrect Usage: python main.py <input file>"
        exit(1)

    f = open(sys.argv[1])
    stmt_set = []
    for line in f:
        stmt = parse.parse(line.strip())
        stmt_set.append(stmt)
    print stmt_set
    conclusion = stmt_set[-1]
    stmt_set = stmt_set[:-1]
    stmt_set.append(parse.parse("~(%s)" % conclusion.__str__()))
    print stmt_set
