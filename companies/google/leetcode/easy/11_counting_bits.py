# https://leetcode.com/problems/counting-bits/
'''
338. Counting Bits

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
'''

#########################################################################################
# Using builtin functions
# TC: O(n log n)
# SC: O(1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            output.append(bin(i).count('1'))
        return output
      
#########################################################################################
# pop count
# TC: O(n log n)
# SC: O(1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def pop_count(x: int) -> int:
            count = 0
            while x != 0:
                x &= x - 1 # zeroing out the least significant nonzero bit
                count += 1
            return count
            
        ans = [0] * (n + 1)
        for x in range(n + 1):
            ans[x] = pop_count(x)
    
        return ans       
    
#########################################################################################
# DP + MSB
# TC: O(n)
# SC: O(1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        x = 0
        b = 1
        
        # [0, b) is calculated
        while b <= n:
            # generate [b, 2b) or [b, n) from [0, b)
            while x < b and x + b <= n:
                ans[x + b] = ans[x] + 1
                x += 1
            x = 0 # reset x
            b <<= 1 # b = 2b
            
        return ans  
      
#########################################################################################
# DP + LSB
# TC: O(n)
# SC: O(1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            # x // 2 is x >> 1 and x % 2 is x & 1
            ans[x] = ans[x >> 1] + (x & 1) 
        return ans 
      
#########################################################################################
# DP + last set
# TC: O(n)
# SC: O(1)

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans 
