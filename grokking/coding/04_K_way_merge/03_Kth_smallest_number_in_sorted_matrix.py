#
'''
Given an N * N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

Example 1:

Input: Matrix=[
    [2, 6, 8], 
    [3, 7, 10],
    [5, 8, 11]
  ], 
  K=5
Output: 7
Explanation: The 5th smallest number in the matrix is 7.
'''

##################################################################################################################################
# minheap
# TC: O(N log k)
# SC: O(k)

from heapq import *

def find_Kth_smallest(matrix, k):
  minheap = []

  # put first element of each row into minheap
  for i in range(min(k, len(matrix))):
    heappush(minheap, (matrix[i][0], 0, matrix[i]))

  numberCount, number = 0, 0
  while minheap:
      number, i, row = heappop(minheap)
      numberCount += 1
      if numberCount == k: break
      
      if len(row) > i+1:
          heappush(minheap, (row[i+1], i+1, row))
  return number


def main():
  print("Kth smallest number is: " +
        str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5)))


main()

'''
Output
1.02s
Kth smallest number is: 7
'''
