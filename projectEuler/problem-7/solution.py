''' By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13. What is the 10 001st prime number?'''


def primeNumber(limit):
    primes = [2]
    i = 3
    while len(primes) < limit:
        if all(i % s != 0 for s in primes):
            primes.append(i)
        i = i + 2
    return primes[-1]


if __name__ == "__main__":
    limit = 10001
    print primeNumber(limit)
