'''
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

 

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

1 <= source.length, target.length <= 1000
source and target consist of lowercase English letters.
'''

###############################################################################################################
# TWO POINTERS
# TC: O(N), SC: O(1)
'''
This one is really simple. 
We have two pointers, one to track our source(j) and one to track our target(i). 
We compare our chars at our respective pointers, and if they match we increment both source(j) and target(i), 
if they don't match then we just increment source(j) pointer. 
If source(j) pointer goes above the length of source that means we have to increase our result by 1 because we have to match with a new source.

We handle the -1 exception right at the start, although it can be handled in the while loop itself by always querying if not target[i] in source.
'''

# TC: O(MN) or O(1) ?
# SC: O(1)
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        for t in target:
            if not t in source:
                return -1
        
        result = 1
        i, j = 0, 0
        
        while i < len(target):
            if j >= len(source):
                j = 0
                result += 1
            if target[i] == source[j]:
                i += 1
            j += 1
            
        return result
        
