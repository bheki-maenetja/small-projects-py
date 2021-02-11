# Basic functions to find the greatest common denominator of two positive integers

# Iterative Solution
def gcdIter(a,b):
    test_value = min(a,b)
    while not (a % test_value == 0 and b % test_value == 0):
        test_value -= 1
    return test_value

# Recursive Solution (Euclid's Algorithm)
def gcdRecur(a,b):
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)