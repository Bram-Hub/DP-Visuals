import parse


# class for holding a logic Statement
class Statement:
    # initilize the Statement
    def __init__(self, kind, value1, value2=None):
        self.type = kind  # statement type (lit, ~, v, ^, ->, <->)
        self.values = [value1, value2]  # value2 is None if the type/connector is not binary

    # for printing / outputing the statement
    def __str__(self):
        if self.type == "lit":
            return "%s" % self.value1()
        elif self.type == "~":
            return "~(%s)" % self.value1()
        else:
            return "%s(%s, %s)" % (self.type, self.value1(), self.value2())

    # for print / outputing the statement
    def __repr__(self):
        return self.__str__()

    # quick & dirty equality operator
    def __eq__(self, other):
        return self.__str__() == other.__str__()

    # returns the "left" half of the statement (or the only part if connector is non-binary)
    def value1(self):
        return self.values[0]

    # returns the "right" half of the statement
    def value2(self):
        return self.values[1]

    # returns a list of the atoms in a statement (Statement(~(Av~B)).contains() == [A, B])
    def contains(self):
        if self.type == "lit":
            return [self.value1()]
        elif self.type == "~":
            return self.value1().contains()
        else:
            c = self.value1().contains()
            c.extend(self.value2().contains())
            return c

    # recursively reduces a statement based on a second statement
    def reduce(self, stmt):
        opp = None
        # determine the opposite of stmt
        if stmt.type == "lit":
            opp = parse.parse("~(%s)" % stmt.__str__())
        else:
            opp = stmt.value1()

        # if this statement is the same as the one we are reducing on then this statment is True
        if self == stmt:
            return True
        # if this statement is the negation of the one we are reducing on, this statement is False
        elif self == opp:
            return False
        else:
            if self.type == "lit":  # the statement is a literal
                # can't recurse any farther, so just return self
                return self

            elif self.type == "~":  # the statement is a negation
                # reduce whatever we are negating first
                new_v1 = self.value1().reduce(stmt)

                if type(new_v1) == bool:  # the new statement was a boolean
                    # return its opposite
                    return not new_v1
                else:
                    # return the negation of whatever we got back
                    return Statement("~", new_v1)
            else:
                # reduce the two components of the statement first
                new_v1 = self.value1().reduce(stmt)
                new_v2 = self.value2().reduce(stmt)

                if self.type == "v":  # the statement was a disjunction
                    if new_v1 is True or new_v2 is True:
                        # either was True, so return whole is True
                        return True
                    elif new_v1 is False:
                        # first was False, return second
                        return new_v2
                    elif new_v2 is False:
                        # second was False, return first
                        return new_v1

                elif self.type == "^":  # the statement was a conjuction
                    if new_v1 is False or new_v2 is False:
                        # either is False, return False
                        return False
                    elif new_v1 is True:
                        # first is True, return second
                        return new_v2
                    elif new_v2 is True:
                        # second is True, return first
                        return new_v1

                elif self.type == "->":  # the statement was an implication
                    if new_v1 is True:
                        # first is true, return second
                        return new_v2
                    elif new_v1 is False:
                        # first is False, return True
                        return True
                    elif new_v2 is True:
                        # second is True, return True
                        return True
                    elif new_v2 is False:
                        # second is False, return negation of first
                        return Statement("~", new_v1)

                elif self.type == "<->":  # the statement was a biconditional
                    if new_v1 is True:
                        # first is True, return second
                        return new_v2
                    elif new_v1 is False:
                        # first is False, return negation of second
                        return Statement("~", new_v2)
                    elif new_v2 is True:
                        # second is True, return first
                        return new_v1
                    elif new_v2 is False:
                        # second is False, return negation of first
                        return Statement("~", new_v1)

                # there were no reductions to a boolean value above, so just return the statement with the reduced parts and the same connector
                return Statement(self.type, new_v1, new_v2)
