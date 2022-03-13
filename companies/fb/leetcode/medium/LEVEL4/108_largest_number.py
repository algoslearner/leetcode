'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''

# Sorting via Custom Comparator 
# TC: O(n log n)
# SC: O(n)

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
 


#######
# METHOD-2:
'''
If we use the default string comparator of sort(), and concatenate sorted strings,
cases as ['3', '30'] will fail for '3' < '30' but we want '330' rather than '303'.
If we use customized cmp_func such that string x is smaller than string y if x + y < y + x, '30' < '3', we will get '330' at last.
'''

from functools import cmp_to_key

class Solution:        
    def largestNumber(self, nums):
        
        def cmp_func(x, y):
            """Sorted by value of concatenated string increasingly."""
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1
            
        # Build nums contains all numbers in the String format.
        nums = [str(num) for num in nums]
        
        # Sort nums by cmp_func decreasingly.
        nums.sort(key = cmp_to_key(cmp_func), reverse = True)
        
        # Remove leading 0s, if empty return '0'.
        return ''.join(nums).lstrip('0') or '0'
        if largest_num[0] == '0':
            return '0'
        else:
            return largest_num
