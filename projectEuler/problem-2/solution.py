#!/usr/bin/env python

'''
Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms
in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.'''


from commonLibs.timer import Timer

@profile
def solution_1(limit):
    ''' Fibonacci series.
    '''
    start = 1
    offset = 0
    list_to_sum = []

    while start < limit:
        start, offset = start + offset, start
        list_to_sum.append(offset)

    return sum(list_to_sum[2::3])

@profile
def solution_2(limit):
    ''' Fibonacci series.
    '''
    start = 1
    offset = 0
    total = 0

    while start < limit:
        start, offset = start + offset, start
        if offset % 2 == 0:
            total += offset

    return total


if __name__ == "__main__":
    limit = 4000000
    with Timer() as T:
        print solution_1(limit)
    print "Elapsed time for solution_1: %f" % T.timeElapsed

    with Timer() as T:
        print solution_2(limit)
    print "Elapsed time for solution_2: %f" % T.timeElapsed
