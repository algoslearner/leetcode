#
'''
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times. 
   
Example 2:

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.
 
Example 3:

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
'''

####################################################################################################################################
# binary search
# TC: O(log n)
# SC: O(1)

def count_rotations(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2

    # if mid is greater than the next element
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1

    # if mid is smaller than the previous element
    if mid > start and arr[mid - 1] > arr[mid]:
      return mid

    if arr[start] < arr[mid]:  # left side is sorted, so the pivot is on right side
      start = mid + 1
    else:  # right side is sorted, so the pivot is on the left side
      end = mid - 1

  return 0  # the array has not been rotated


def main():
  print(count_rotations([10, 15, 1, 3, 8]))
  print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
  print(count_rotations([1, 3, 8, 10]))


main()

'''
Output
2
5
0
'''

############################################################################################################################
# How do we find the rotation count of a sorted and rotated array that has duplicates too?

def count_rotations_with_duplicates(arr):
  start, end = 0, len(arr) - 1
  while start < end:
    mid = start + (end - start) // 2
    # if element at mid is greater than the next element
    if mid < end and arr[mid] > arr[mid + 1]:
      return mid + 1
    # if element at mid is smaller than the previous element
    if mid > start and arr[mid - 1] > arr[mid]:
      return mid

    # this is the only difference from the previous solution
    # if numbers at indices start, mid, and end are same, we can't choose a side
    # the best we can do is to skip one number from both ends if they are not the smallest number
    if arr[start] == arr[mid] and arr[end] == arr[mid]:
      if arr[start] > arr[start + 1]:  # if element at start+1 is not the smallest
        return start + 1
      start += 1
      if arr[end - 1] > arr[end]:  # if the element at end is not the smallest
        return end
      end -= 1
    # left side is sorted, so the pivot is on right side
    elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
      start = mid + 1
    else:  # right side is sorted, so the pivot is on the left side
      end = mid - 1

  return 0  # the array has not been rotated


def main():
  print(count_rotations_with_duplicates([3, 3, 7, 3]))


main()

'''
Output
3
'''
