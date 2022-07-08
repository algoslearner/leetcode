#
'''
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
'''

##############################################################################################################################
# two pointers
# TC: O(n)
# SC: O(1)

def make_squares(arr):
  squares = [0 for i in range(n)]
  left = 0
  right = len(arr) - 1
  
  i = len(arr) - 1
  while left <= right:
    left_square = arr[left] * arr[left]
    right_square = arr[right] * arr[right]
    if left_square > right_square:
      squares[i] = left_square
      left += 1
    else:
      squares[i] = right_square
      right -= 1
    i -= 1
    
  return squares 
