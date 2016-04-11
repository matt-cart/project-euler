"""
Project Euler - Problem 10

SOLVE
"""
import utils

def primesSieve(prime_dict):
    limit = len(prime_dict) 
    for (i, isprime) in enumerate(prime_dict):
        if isprime:
            for n in xrange(i*i, limit, i):
                prime_dict[n] = False
    return prime_dict

if __name__ == "__main__":
    top_num = 2000000
    prime_dict = [True] * top_num
    prime_dict[0] = prime_dict[1] = False
    prime_dict = primesSieve(prime_dict)
    running_sum = 0
    for i,isprime in enumerate(prime_dict):
        if isprime:
            running_sum += i
    print prime_dict
    print running_sum
