#!/usr/bin/env python


def getListOfPythagoreanTriplet(pivot=1, limit=1000):
    a = 1
    b = 1
    c = 0
    m = 2
    while(c < limit):
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n
            total = a + b + c
            if total == 1000:
                print a*b*c
        m = m+1


if __name__ == "__main__":
    limit = 1000
    getListOfPythagoreanTriplet(limit=limit)
