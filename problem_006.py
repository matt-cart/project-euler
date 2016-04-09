"""
Project Euler - Problem 6

SOLVED
"""
if __name__ == "__main__":
    end_num = 100
    square_of_sums = sum([(i+1) for i in range(0, end_num)])**2
    sum_of_squares = sum([(i+1)**2 for i in range(0, end_num)])
    print square_of_sums - sum_of_squares
