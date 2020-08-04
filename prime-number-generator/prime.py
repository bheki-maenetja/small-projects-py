def genPrimes():
    primes = [2,3,5,7,11]
    for n in range(2, 10**6):
        # print(all(n % p != 0 for p in primes))
        if n in primes:
            yield n
        elif all(n % p != 0 for p in primes):
            primes.append(n)
            yield n

gen = genPrimes()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))