# https://leetcode.com/problems/counting-elements/
'''
Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately.

 

Example 1:

Input: arr = [1,2,3]
Output: 2
Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
Example 2:

Input: arr = [1,1,3,3,5,5,7,7]
Output: 0
Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.
 

Constraints:

1 <= arr.length <= 1000
0 <= arr[i] <= 1000
'''

#####################################################################################################################################
# hashset
# TC: O(N)
# SC: O(N)

class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        hashset = set(arr)
        for x in arr:
            if x + 1 in hashset:
                count += 1
        return count
      
#####################################################################################################################################
# sort + two pointers
# TC: O(N log N)
# SC: O(1)

class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr.sort()
        
        count = 0
        left = 0
        right = 0
        while right < len(arr):
            if arr[left] + 1 == arr[right]:
                count += right - left
                left = right
            elif arr[left] + 1 < arr[right]:
                left += 1
            else:
                right += 1
        return count
