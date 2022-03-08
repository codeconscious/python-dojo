class Tools:
    def __init__(self, base):
        self.base = base

    def exponents(self, exponent):
        result = self.base
        for n in range(1, exponent):
            result *= self.base
        print("%s to the %sth power is %s" % (self.base, exponent, result))

    @staticmethod
    def exponentsWithBase(customBase, exponent):
        result = customBase
        for n in range(1, exponent):
            result *= customBase
        print("%s to the %sth power is %s" % (customBase, exponent, result))

tools = Tools(5)
tools.exponents(3)
tools.exponentsWithBase(2, 10)
