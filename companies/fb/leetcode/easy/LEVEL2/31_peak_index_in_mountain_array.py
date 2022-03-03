'''
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
 

Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.
 

Follow up: Finding the O(n) is straightforward, could you find an O(log(n)) solution?
'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # return arr.index(max(arr))
    
        # Linear search, TC : O(n), SC: O(1)
        '''
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return i
        '''
        
        # Binary search, TC: O(log n), SC: O(1)
        left = 0
        right = len(arr)-1
        while left < right:
            mid = left + (right - left)// 2
            # mid = (left + right) // 2
            if arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                left = mid
            else:
                right = mid
            
        
