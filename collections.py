class XPerson:
    def __init__(self, heroName, normalName, powers):
        self.heroName = heroName
        self.normalName = normalName
        self.powers = powers

    def describe(self):
        return "> %s (%s) has the power of %s." % (self.heroName, self.normalName, self.powers)

xmen = {}
xmen["cyclops"] = XPerson("Cyclops", "Scott Summers", "optic blasts")
xmen["magneto"] = XPerson("Magneto", "Erik Lehnsherr", "magnetism")
xmen["jubilee"] = XPerson("Jubilee", "Jubilation Lee", "pyrotechnic energy blasts")
xmen["storm"] = XPerson("Storm", "Ororo Munroe", "weather manipulation")
del(xmen["magneto"]) # Or: xmen.pop("magneto")
for x, y in xmen.items():
    print(y.describe())


sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)
print(word_lengths)