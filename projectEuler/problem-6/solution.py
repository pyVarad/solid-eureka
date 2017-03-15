'''The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385 .The square of the sum of the first ten natural
numbers is, (1 + 2 + ... + 10)2 = 552 = 3025 Hence the difference between the
sum of the squares of the first ten natural numbers and the square of the
sum is 3025 - 385 = 2640. Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
'''

import math


def sumOfSquares(limit):
    sumOf_Squares = (limit * (limit+1) * (2*limit + 1))/6
    return sumOf_Squares


def squareOfSum(limit):
    total = (limit * (limit + 1))/2
    return math.pow(total, 2)


def diff(limit):
    t1 = squareOfSum(limit)
    t2 = sumOfSquares(limit)
    return t1 - t2


if __name__ == "__main__":
    print diff(100)
