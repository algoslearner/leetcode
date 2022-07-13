# 
'''
Given an array of n-1 integers in the range from 1 to n, find the one number that is missing from the array.
'''

####################################################################################################################
# sum of array
# TC: O(n)
# SC: O(1)
# While finding the sum of numbers from 1 to n, we can get integer overflow when n is large.

def find_missing_number(arr):
  n = len(arr) + 1
  # find sum of all numbers from 1 to n.
  s1 = 0
  for i in range (1, n+1):
    s1 += i

  # subtract all numbers in input from sum.
  for i in arr:
    s1 -= i
  
  # s1, now, is the missing number
  return s1

####################################################################################################################
# xor
# TC: O(n)
# SC: O(1)

def find_missing_number(arr):
  n = len(arr) + 1
  # x1 represents XOR of all values from 1 to n
  x1 = 1
  for i in range(2, n+1):
    x1 = x1 ^ i

  # x2 represents XOR of all values in arr
  x2 = arr[0]
  for i in range(1, n-1):
    x2 = x2 ^ arr[i]
  
  # missing number is the xor of x1 and x2
  return x1 ^ x2  
