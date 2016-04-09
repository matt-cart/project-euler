"""
Project Euler - Problem 2

SOLVED
"""

def generateFibonacci(upper_bound):
    """
    Generate a list of Fibonacci numbers smaller than an upper bound.
    """
    fibs = [0]
    latest = 1
    while latest < upper_bound:
        fibs.append(latest)        
        latest = fibs[-1] + fibs[-2]
    return fibs


def findEvens(lst):
    """
    Return the list of even integers in an input list of integers.
    """
    evens = []
    for el in lst:
        if el % 2 == 0:
            evens.append(el)
    return evens


if __name__ == "__main__":
    fibonacci_lst = generateFibonacci(4000000)
    even_fibs = findEvens(fibonacci_lst)
    print sum(even_fibs)
