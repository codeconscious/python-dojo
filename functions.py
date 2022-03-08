class Tools:
    def exponentsInstance(self, base, exponent):
        output = base
        for n in range(1, exponent):
            output *= base
        return output

    @staticmethod
    def exponentsStatic(base, exponent):
        output = base
        for n in range(1, exponent):
            output *= base
        return output

tools = Tools()
print(tools.exponentsInstance(2, 10))
print(tools.exponentsStatic(2, 10))
