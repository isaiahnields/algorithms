from math import sqrt

def primes(start, end):
    start = start if start >= 2 else 2
    for n in range(start, end):
        for c in range(2, int(sqrt(n) + 1)):
            if n % c == 0:
                break
        else:
            yield n

for n in primes(2, 10000000):
    print(n)