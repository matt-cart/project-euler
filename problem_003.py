"""
Project Euler - Problem 3

SOLVED
"""
import utils

def findLargestPrime(x):
    return max(utils.findPrimeFactors(x))

if __name__ == "__main__":
    input_num = 600851475143
    print findLargestPrime(input_num)
