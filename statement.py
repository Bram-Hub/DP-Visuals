import parse


class Statement:
    def __init__(self, kind, value1, value2=None):
        self.type = kind
        self.values = [value1, value2]

    def __str__(self):
        if self.type == "lit":
            return "%s" % self.value1()
        elif self.type == "~":
            return "~(%s)" % self.value1()
        else:
            return "%s(%s, %s)" % (self.type, self.value1(), self.value2())

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __deepcopy__(self):
        return parse.parse(self.__str__())

    def value1(self):
        return self.values[0]

    def value2(self):
        return self.values[1]

    def contains(self):
        if self.type == "lit":
            return [self.value1()]
        elif self.type == "~":
            return self.value1().contains()
        else:
            c = self.value1().contains()
            c.extend(self.value2().contains())
            return c

    def reduce(self, stmt):
        opp = None
        if stmt.type == "lit":
            opp = parse.parse("~(%s)" % stmt.__str__())
        else:
            opp = stmt.value1()

        if self == stmt:
            return True
        elif self == opp:
            return False
        else:
            if self.type == "lit":
                return self
            elif self.type == "~":
                new_v1 = self.value1().reduce(stmt)
                if type(new_v1) == bool:
                    return not new_v1
                else:
                    return Statement("~", new_v1)
            else:
                new_v1 = self.value1().reduce(stmt)
                new_v2 = self.value2().reduce(stmt)
                if self.type == "v":
                    if new_v1 is True or new_v2 is True:
                        return True
                    elif new_v1 is False:
                        return new_v2
                    elif new_v2 is False:
                        return new_v1
                    else:
                        return Statement("v", new_v1, new_v2)
                elif self.type == "^":
                    pass
                elif self.type == "->":
                    pass
                elif self.type == "<->":
                    pass
        return None
