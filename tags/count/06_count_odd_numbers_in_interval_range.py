#
'''
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9
'''

####################################################################################################################################
# linear scan
# TC: O(n)
# SC: O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high + 1):
            if n % 2 != 0:
                count += 1
        return count
      
####################################################################################################################################
# math
# TC: O(1)
# SC: O(1)

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            return (high - low + 1) // 2
        return (high - low) // 2 + 1
