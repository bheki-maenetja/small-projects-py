def infinitePrimes():
    num = 1
    while True:
        num += 1
        if not any(i for i in range(2, num) if num % i == 0):
            yield num

myGen = infinitePrimes()

def genPrimes(num):
    for n in range(2, num + 1):
        if not any(i for i in range(2, n) if n % i == 0):
            yield n

def genFibbo(num):
    n1, n2 = 0, 1
    for i in range(num + 1):
        n1, n2 = n2, n1+n2
        yield n2

def genSquare(num):
    for n in range(num):
        yield n ** 2

print("hello?")