"""
Project Euler - Problem 10

OPEN
"""
import utils

if __name__ == "__main__":
    top_num = 10
    nums = reversed(range(2, top_num+1))
    primes = []
    for num in nums:
        if num % 2 != 0:
            if num % 3 != 0:
                if num % 5 != 0:
                    if utils.isPrime(num):
                        print num
                        primes.append(num)
