"""
Project Euler - Problem 4

SOLVED
"""
import math

def palindrome(i):
    s = str(i)
    l = list(s)
    start = 0
    end = -1
    while start < math.sqrt(len(l)):
        if l[start] == l[end]:
            start += 1
            end -= 1
        else:
            return False
    return True

if __name__ == "__main__":
    products = []
    for k in reversed(range(100, 1000)):
        for j in reversed(range(100, 1000)):
            products.append(k*j)
    products = sorted(products, reverse=True)
    for i in products:
        if palindrome(i):
            print i
            break

