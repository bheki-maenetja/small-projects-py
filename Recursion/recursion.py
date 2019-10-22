def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(5))

def countDownFrom(n):
    print(n)
    if n > 0:
        countDownFrom(n-1)

countDownFrom(10)

def countUpTo(n):
    if n > 0:
        countUpTo(n-1)
    print(n)

countUpTo(10)
