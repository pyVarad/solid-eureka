""" The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.Find the sum of all
the primes below two million."""


def sumPrimes(n):
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        if sieve[p]:
            sum += p
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print sumPrimes(2000000)
