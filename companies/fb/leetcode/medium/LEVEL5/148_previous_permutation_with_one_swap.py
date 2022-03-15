'''
Given an array of positive integers arr (not necessarily distinct), return the lexicographically largest permutation that is smaller than arr, that can be made with exactly one swap (A swap exchanges the positions of two numbers arr[i] and arr[j]). If it cannot be done, then return the same array.

 

Example 1:

Input: arr = [3,2,1]
Output: [3,1,2]
Explanation: Swapping 2 and 1.
Example 2:

Input: arr = [1,1,5]
Output: [1,1,5]
Explanation: This is already the smallest permutation.
Example 3:

Input: arr = [1,9,4,6,7]
Output: [1,7,4,6,9]
Explanation: Swapping 9 and 7.
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i] <= 104
'''

########################################################################
# https://leetcode.com/problems/previous-permutation-with-one-swap/discuss/328779/Python-O(N)-with-explanation
# TC; O(N), SC: O(1)
'''
Go from right side to left until numbers are getting smaller.
Go from left side to right until the number is both higher than previous and smaller than the number on the leftmost side.
Swap leftmost with the one from (2) and return.
'''

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        a= arr       
        
        left = len(a)-1 
        while left>0 and a[left-1]<=a[left]:
            left-=1
        if left==0: return a
        
        right = left
        for i in range(left,len(a)):
            if a[i]>a[right] and a[i]<a[left-1]: right = i
        a[right],a[left-1]=a[left-1],a[right]
        
        return a
        
