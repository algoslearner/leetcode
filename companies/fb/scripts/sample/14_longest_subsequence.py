# https://leetcode.com/discuss/interview-question/1353596/Facebook-or-Phone-Screen/1021809
'''
Find longest subsequence in s that repeats n times. If multiple output any.

Examples:
s = "0011100111" and n = 3 should output "11"
s = "0011100111" and n = 2 should output "00111"
s = "0011100111" and n = 4 should output "1" or "0"

Clarification: For a subsequence to "repeat" it means that if the first sequence is the starts at index i and ends at index j, then the next sequence must start after index j.

Had no idea how to solve it or start it. I'm pretty sure I failed.

I should also add that this was the hint version of the question. The original question was given a string s, find a subsequence k that gives maximum score where score is given as len(k)*(# of repetitions of k).
'''

########## SOLUTION (hard)
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/


##########################################################################################
# https://leetcode.com/discuss/interview-question/1509439/facebook-phone-screen-new-grad
'''
Length of longest subsequesnce increasing by 1 (it can skip some inputs but is still taking them in order)
ex - 8,5,6,2,0,3,4,4,5,7,1 output is 2,3,4,5
I could not solve this. Just told the brute force approach which will be very costly.
'''

########## SOLUTION COMMENTS
'''
For Q2: Use the map and search for previous number in the map and maintain the mx_seq_len and mx_seq_end variables during iteration.
Finally generate the sequence using the mx_seq_len and mx_seq_end variables
TC: O(n) Space Complexity: O(n)
'''

def longestConsecutiveSubsequence(arr):
    mx_seq_len, mx_seq_end = 0, 0
    mp = {}
    for a in arr:
        mp[a] = 1 + (mp[a - 1] if a - 1 in mp else 0)
        if mx_seq_len < mp[a]:
            mx_seq_len = mp[a]
            mx_seq_end = a
    return list(range(mx_seq_end - mx_seq_len + 1, mx_seq_end + 1))

longestConsecutiveSubsequence([8, 5, 6, 2, 0, 3, 4, 4, 5, 7, 1])
longestConsecutiveSubsequence([1, 3, 2, 3, 4, 5, 1, 6])

###### SOLUTION (medium)
# https://leetcode.com/problems/longest-increasing-subsequence/solution/
'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''

############################
# METHOD-1 (TC: O(n2), SC: O(n)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
 
############################
 # Method-2 use binary search. TC: O(n log n), SC: O(n)
  
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            i = bisect_left(sub, num)

            # If num is greater than any element in sub
            if i == len(sub):
                sub.append(num)
            
            # Otherwise, replace the first element in sub greater than or equal to num
            else:
                sub[i] = num
        
        return len(sub)
#################################################################################################################################################

# READ
# https://leetcode.com/problems/longest-increasing-subsequence/solution/
# https://leetcode.com/problems/longest-consecutive-sequence/
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
      # Here put difference = 1 and you would have the answer (got the idea from @northystar's solution)
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/
