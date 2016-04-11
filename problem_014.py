"""
Project Euler - Problem 14

SOLVED
"""

def collatz(lst, n):
    if n % 2 == 0 and n > 1:
        n /= 2
        lst.append(n)
        collatz(lst, n)
    elif n % 2 != 0 and n > 1:
        n = 3 * n + 1
        lst.append(n)
        collatz(lst, n)
    return lst

if __name__ == "__main__":
    longest_length = 0
    starting_number = 0
    for i in reversed(range(1, 1000000)):
        start = i
        collatz_list = collatz([start], start)
        collatz_length = len(collatz_list)
        if collatz_length > longest_length:
            longest_length = collatz_length
            starting_number = start
    print starting_number

