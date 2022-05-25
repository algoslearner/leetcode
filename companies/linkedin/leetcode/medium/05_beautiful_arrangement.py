# https://leetcode.com/problems/beautiful-arrangement/
'''
526. Beautiful Arrangement

Suppose you have n integers labeled 1 through n. 
A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct.

 

Example 1:

Input: n = 2
Output: 2
Explanation: 
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
Example 2:

Input: n = 1
Output: 1
 

Constraints:

1 <= n <= 15
'''

##################################################################################################
# backtracking
# https://leetcode.com/problems/beautiful-arrangement/discuss/99738/Easy-Python-~230ms

class Solution:
    def countArrangement(self, n: int) -> int:
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i - 1, X - {x})
                       for x in X
                       if x % i == 0 or i % x == 0)
        return count(n, set(range(1, n + 1)))

##################################################################################################
# DFS - permutation
# https://leetcode.com/problems/beautiful-arrangement/discuss/1000324/Python-Permutation-Solution
'''
It took a while for me to understand this question. In the end all they were asking for was to find a permutation of n numbers that satisfy one of these conditions. EIther the number at index + 1 is divisible by the index + 1 or index + 1 is divisible by the number. Also a much better example would have been to show what happens with 3 numbers.

I'll just put one example of where this fails because it seems like a better example.

[1,3,2] - This fails because 3 is not divisible by index + 1 (2) and also index + 1 (2) is not divisible by 3.

Generate the array of numbers that will be used to create permutations of 1 to n (n inclusive) ex: 3 will become [1,2,3]
Iterate through all elements in the list and compare it to i which is initialized at 1 to avoid the while index + 1 thing.
If the number is divisible by i or i is divisible by the number, remove the number from nums and continue generating the permutation.
If a full permutation is generated (i == n+1, aka went past the index) then we have one solution. Add that to the result.
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        
        self.res = 0
        nums = [i for i in range(1, n+1)]
        
        def dfs(nums: list, i: int = 1):
            if i == n+1: 
                self.res += 1
                return
            
            for j, num in enumerate(nums):
                if not(num % i and i % num):
                    dfs(nums[:j] + nums[j+1:], i+1)
            
        dfs(nums)
        return self.res
