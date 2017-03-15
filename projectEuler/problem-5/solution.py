'''

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
'''

import math

def getPrime(limit):
    i = 2
    res = None
    while(i < limit):
        if limit % i == 0:
            i = 2
            res = None
            break
        else:
            i = i + 1
            res = limit
    return res


def getPrimeLessThanLimit(upperlimit):
    availableList = [2]
    while upperlimit:
        res = getPrime(upperlimit)
        if res:
            availableList.append(res)
        upperlimit = upperlimit - 1
    return availableList


def getHighestExponentOfEachFactor(limit):
    res = 1
    for i in getPrimeLessThanLimit(limit):
        j = 0
        while pow(i, j+1) < limit:
            j = j+1
        res = res * pow(i,j)
    return res



if __name__ == "__main__":
    #getPrimeLessThanLimit(10)
    #getPrime(9)
    print getHighestExponentOfEachFactor(10000)
