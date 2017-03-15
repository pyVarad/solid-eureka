#!/usr/bin/env python

FibanocciSeries = [1]

def factorial(n):
    if n==0:
        return 1
    else:
       return n*factorial(n-1)


def fibanocci(a=1, b=1, limit=100000000000000000000000000000000000000000000000000):
    if limit > b:
       a, b = b, a+b
       FibanocciSeries.append(a)
       return fibanocci(a, b, limit-1)


if __name__ == "__main__":
#   fibanocci()
#   print FibanocciSeries
    print factorial(1000)
