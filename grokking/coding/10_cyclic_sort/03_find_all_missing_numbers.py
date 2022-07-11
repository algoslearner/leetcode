# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
'''
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates, which means some numbers will be missing. 

Find all those missing numbers.

Example 1:

Input: [2, 3, 1, 8, 2, 3, 5, 1]
Output: 4, 6, 7
Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.
Example 2:

Input: [2, 4, 1, 2]
Output: 3
Example 3:

Input: [2, 3, 2, 1]
Output: 4
'''

##############################################################################################################################
# hashmap
# TC: O(n)
# SC: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1
        
        output = []
        for num in range(1, len(nums)+1):
            if num not in hashmap:
                output.append(num)
        return output
      
##############################################################################################################################
# math
# TC: O(n)
# SC: O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        
        res = []
        for i,n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        
        return res

##############################################################################################################################
# cyclic sort
# TC: O(n)
# SC: O(1)

def find_all_missing_numbers(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
   
  output = []
  for i in range(len(nums)):
    if nums[i] != i + 1:
      output.append(i + 1)
  
  return output
    
