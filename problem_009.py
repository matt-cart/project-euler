"""
Project Euler - Problem 9

SOLVED
"""

if __name__ == "__main__":
    num_to_find = 1000
    for c in range(0, 1000):
        for b in range(0, c):
            for a in range(0, b):
                if a < b and b < c:
                    if a**2 + b**2 == c**2:
                        if a + b + c == num_to_find:
                            print a * b * c
