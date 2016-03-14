from parse import parse


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

    def __eq__(self, other):
        return self.__str__() == other.__str__()

    def __deepcopy__(self):
        return parse(self.__str__())

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
