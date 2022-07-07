#
'''
Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once. 
The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).

Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].
'''

###################################################################################################################
# two pointers
# TC: O(N)
# SC: O(1)

def remove_duplicates(arr):
  index = 0
  for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
      arr[index] = arr[i]
      index += 1
   return index

