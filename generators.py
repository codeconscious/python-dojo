import random

# Return 7 random numbers
def lottery():
    for i in range(6):
        yield random.randint(1, 40)
    yield random.randint(-20, -1)

for random_number in lottery():
    print("• %d" % (random_number))


def char_generator(count):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(count):
        yield letters[random.randint(0, 25)]

# Print 75 letters, separating them into groups of 5 for legibility.
output = ""
for index, letter in enumerate(char_generator(75)): # Use enumerate to get the index
    output += letter
    if (index % 5 == 4):
        output += " "
print(output)
