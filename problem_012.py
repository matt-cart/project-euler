"""
Project Euler - Problem 12

SOLVED
"""
import utils

if __name__ == "__main__":
    triangle_num = 1
    num = 1
    threshold = 500
    while True:
        if len(utils.findFactors(triangle_num)) >= 500:
            print triangle_num
            break
        num += 1
        triangle_num += num
        
