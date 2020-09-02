import time

# Factorial - A simple function to find n!
def factorial(n):
  if n == 0:
      result = 1
  else:
      result = n * factorial(n-1)
  return result

# Timer - A function to find the runtime of any function
def blockFunc():
  start_time = time.time()
  factorial(996)
  end_time = time.time()
  print(f'Runtime: {(end_time - start_time) * 1000} ms')

# Count Down - Count down from n to 0
def countDownFrom(n):
    print(n)
    if n > 0:
        countDownFrom(n-1)

# Count Up - Count up from 0 to n
def countUpTo(n):
    if n > 0:
        countUpTo(n-1)
    print(n)

# Sum List - Finds the sum all elements in a list (assuming all elements are numeric)
def sumNumList(arr, index = 0, num_sum = 0):
  if index == len(arr):
    return num_sum
  num_sum += arr[index]
  return sumNumList(arr, index + 1, num_sum)

# Max Num - Finds the biggest number in a list
def maxNum(arr, index = 0, max_num = 0):
  if index == len(arr): 
    return max_num
  if arr[index] > max_num: 
    max_num = arr[index]
  index += 1
  return maxNum(arr, index, max_num)

# Fibbo - Returns a list of n fibbonacci numbers
def fibbo(n, arr = [1,1], i = 1):
  if len(arr) == n or n <= 2: 
    return arr[-1]
  arr.append(arr[i] + arr[i-1])
  i += 1
  return fibbo(n, arr, i)

# Last Character - Returns the last character in a string
def lastChar(string, i = 0):
  if string == '': 
    return string
  if i == len(string) - 1: 
    return string[i]
  return lastChar(string, i + 1)

print(lastChar(''))

# Checks to see if character is in a string
def isIn(char, aStr):
  print(char, aStr)
  if aStr == '':
    return False
  elif len(aStr) == 1 and aStr != char:
    return False
  elif char == aStr:
    return True
  elif char == aStr[len(aStr) // 2]:
    return True
  elif char > aStr[len(aStr) // 2]:
    return isIn(char, aStr[len(aStr) // 2:])
  elif char < aStr[len(aStr) // 2]:
    return isIn(char, aStr[:len(aStr) // 2])

