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

    def value1(self):
        return self.values[0]

    def value2(self):
        return self.values[1]
