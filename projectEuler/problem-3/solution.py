''' Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''


from commonLibs.timer import Timer
from sympy.ntheory import factorint


def primeNumber_2(n):
    """ Returns  a list of primes < n """
    return all(n % i for i in range(2, n))

@profile
def factor(num):
    ''' Factors of a number
    '''
    for factors in factorint(num).keys():
        if primeNumber_2(factors):
            break
    return factors


if __name__ == "__main__":
    print factor(600851475143)
