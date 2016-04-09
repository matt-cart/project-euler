"""
Project Euler - Problem 7

SOLVED
"""
import utils

if __name__ == "__main__":
    prime_count = 0
    prime_threshold = 10001
    i = 2
    while True:
        if utils.isPrime(i):
            prime_count += 1
            if prime_count == prime_threshold:
                print i
                break
        i += 1
