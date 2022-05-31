import random

def lottery():
    # Returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # Returns a 7th random number
    yield random.randint(-20, -1)

for random_number in lottery():
    print("• %d" % (random_number))
