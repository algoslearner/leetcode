#
'''
Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target 
where i, j, and k are three different indices. 

Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
'''

##########################################################################################################################################
# TC: O(N^2)
# SC: O(N)

def triplet_with_smaller_sum(arr, target):
  arr.sort()
  count = 0
  for i in range(len(arr)-2):
    count += search_pair(arr, target - arr[i], i)
  return count


def search_pair(arr, target_sum, first):
  count = 0
  left, right = first + 1, len(arr) - 1
  while (left < right):
    if arr[left] + arr[right] < target_sum:  # found the triplet
      # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
      # left and right to get a sum less than the target sum
      count += right - left
      left += 1
    else:
      right -= 1  # we need a pair with a smaller sum
  return count


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()

##########################################################################################################################################
# Problem: Write a function to return the list of all such triplets instead of the count. How will the time complexity change in this case?
# TC: O(N^3)
# SC: O(N)

def triplet_with_smaller_sum(arr, target):
  arr.sort()
  triplets = []
  for i in range(len(arr)-2):
    search_pair(arr, target - arr[i], i, triplets)
  return triplets


def search_pair(arr, target_sum, first, triplets):
  left = first + 1
  right = len(arr) - 1
  while (left < right):
    if arr[left] + arr[right] < target_sum:  # found the triplet
      # since arr[right] >= arr[left], therefore, we can replace arr[right] by any number between
      # left and right to get a sum less than the target sum
      for i in range(right, left, -1):
        triplets.append([arr[first], arr[left], arr[i]])
      left += 1
    else:
      right -= 1  # we need a pair with a smaller sum


def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()



