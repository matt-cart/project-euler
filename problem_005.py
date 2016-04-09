"""
Project Euler - Problem 5

SOLVED
"""
def testAllDivisible(value, max_digit):
    divisibles = reversed(range(1, max_digit+1))
    for d in divisibles:
        if value % d != 0:
            return False
    return True


def smallestMultiple(starting, max_digit):
    value = starting
    while True:
        all_divisible = True
        if testAllDivisible(value, max_digit):
            return value
        else:
            value += max_digit
        


if __name__ == "__main__":
    print smallestMultiple(20, 20)
