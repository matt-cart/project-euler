"""
Project Euler - Problem 1

SOLVED
"""

def findMultiples(upper_bound, multiples_of):
    """
    Return a list of integers smaller than an upper bound that 
    are multiples of a given list of input integers.
    """
    multiples = []
    for i in range(upper_bound):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
    return multiples

if __name__ == "__main__":
    upper_bound = 1000
    multiples_of = [3, 5]
    multiples = findMultiples(upper_bound, multiples_of)
    print sum(multiples)
