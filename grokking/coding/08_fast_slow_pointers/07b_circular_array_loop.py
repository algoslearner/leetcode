# https://leetcode.com/problems/circular-array-loop/
'''
457. Circular Array Loop

You are playing a game involving a circular array of non-zero integers nums. 
Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i:

If nums[i] is positive, move nums[i] steps forward, and
If nums[i] is negative, move nums[i] steps backward.
Since the array is circular, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.

A cycle in the array consists of a sequence of indices seq of length k where:

Following the movement rules above results in the repeating index sequence seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...
Every nums[seq[j]] is either all positive or all negative.
k > 1
Return true if there is a cycle in nums, or false otherwise.

 

Example 1:

Input: nums = [2,-1,1,2,2]
Output: true
Explanation:
There is a cycle from index 0 -> 2 -> 3 -> 0 -> ...
The cycle's length is 3.
Example 2:

Input: nums = [-1,2]
Output: false
Explanation:
The sequence from index 1 -> 1 -> 1 -> ... is not a cycle because the sequence's length is 1.
By definition the sequence's length must be strictly greater than 1 to be a cycle.
Example 3:

Input: nums = [-2,1,-1,-2,-2]
Output: false
Explanation:
The sequence from index 1 -> 2 -> 1 -> ... is not a cycle because nums[1] is positive, but nums[2] is negative.
Every nums[seq[j]] must be either all positive or all negative.
 

Constraints:

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000
nums[i] != 0
 

Follow up: Could you solve it in O(n) time complexity and O(1) extra space complexity?
'''

#####################################################################################################################
# fast and slow pointers
# TC: O(N^2)
# SC: O(1)

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def get_next_index(nums, cur_index, is_positive):
            direction = nums[cur_index] >= 0
            if direction != is_positive:
                return -1
            
            next_index = (cur_index+nums[cur_index])%len(nums)
            if next_index < 0:
                next_index = len(nums) - next_index 
                
            if next_index == cur_index:
                next_index = -1
                
            return next_index
        
        for index in range(len(nums)):
            is_positive = nums[index] >= 0
            fast, slow, = index, index
            while True:
                slow = get_next_index(nums, slow, is_positive)
                fast = get_next_index(nums, fast, is_positive)
                
                if fast != -1:
                    fast = get_next_index(nums, fast, is_positive)
                if slow == -1 or fast == -1:
                    break
                if slow == fast:
                    return True
        return False
      
      
      

#####################################################################################################################
# fast and slow pointers
# TC: O(N)
# SC: O(1)

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        
        for i, num in enumerate(nums):
            # use a distinct marker for each starting point
            mark = str(i)
            
            # explore while node is new, direction is same, and is not self loop
            # note: if node has been marked by a different marker, no need to proceed. This gives O(n) time.
            while (type(nums[i]) == int) and (num * nums[i] > 0) and (nums[i] % len(nums) != 0):
                jump = nums[i] 
                nums[i] = mark
                i = (i + jump) % len(nums)
            
            # if self loop, nums[i] is never marked
            # if nums[i] is marked, a cycle is found
            if nums[i] == mark:
                return True
            
        return False
