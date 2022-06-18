#
'''
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. 
Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
'''

#############################################################################################################
# minheap + binary search
# tc: O(k log k + log N)
# sc: O(k)

from heapq import *

def find_closest_elements(arr, K, X):
      
  index = binary_search(arr, X)
  low = index - K
  high = index + K
  low = max(low, 0)
  high = min(high, len(arr)-1)

  minheap = []
  for i in range(low, high+1):
    heappush(minheap, (abs(arr[i] - X), arr[i]))

  # we need to k elemenets having smallest difference from x
  result = []
  for _ in range(K):
    result.append(heappop(minheap)[1])
  result.sort()
  return result

def binary_search(arr, target):
      low = 0
      high = len(arr) - 1
      while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                  return mid
            elif arr[mid] > target:
                  high = mid - 1
            else:
                  low = mid + 1
      
      if low > 0:
            return low - 1
      return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()

'''
Output
0.8s
'K' closest numbers to 'X' are: [6, 7, 8]
'K' closest numbers to 'X' are: [4, 5, 6]
'K' closest numbers to 'X' are: [5, 6, 9]
'''

#############################################################################################################
# two pointers + binary search
# tc: O(k + log N)
# sc: O(1)

from collections import deque


def find_closest_elements(arr, K, X):
  result = deque()
  index = binary_search(arr, X)
  leftPointer, rightPointer = index, index + 1
  n = len(arr)
  for i in range(K):
    if leftPointer >= 0 and rightPointer < n:
      diff1 = abs(X - arr[leftPointer])
      diff2 = abs(X - arr[rightPointer])
      if diff1 <= diff2:
        result.appendleft(arr[leftPointer])
        leftPointer -= 1
      else:
        result.append(arr[rightPointer])
        rightPointer += 1
    elif leftPointer >= 0:
      result.appendleft(arr[leftPointer])
      leftPointer -= 1
    elif rightPointer < n:
      result.append(arr[rightPointer])
      rightPointer += 1

  return result


def binary_search(arr, target):
      low = 0
      high = len(arr) - 1
      while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == target:
                  return mid
            elif arr[mid] > target:
                  high = mid - 1
            else:
                  low = mid + 1
      
      if low > 0:
            return low - 1
      return low


def main():
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
  print("'K' closest numbers to 'X' are: " +
        str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()

