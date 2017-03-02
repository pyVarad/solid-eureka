#!/usr/bin/env python

'''
if we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all
the multiples of 3 or 5 below 1000.
'''

from commonLibs.timer import Timer


def solution(limit):
    """
    Find the numbers divisible by 3 and 5 and add them
    """
    sum = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            sum += num

    return sum


def solution_effective(limit, divisor):
    """
    Effective Algorithm
    """
    target = (limit-1) // divisor
    sum_of_all = divisor * (target * (target + 1))/2
    return sum_of_all


if __name__ == "__main__":
    limit = 1000
    with Timer() as T:
        print solution(limit)
    print "Completed in %f" % T.timeElapsed

    with Timer() as T:
        result = solution_effective(limit, 3) + \
                solution_effective(limit, 5) -  \
                solution_effective(limit, 15)
        print result
    print "Completed in %f" % T.timeElapsed
