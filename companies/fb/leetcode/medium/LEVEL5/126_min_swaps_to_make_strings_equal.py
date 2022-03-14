'''
You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

 

Example 1:

Input: s1 = "xx", s2 = "yy"
Output: 1
Explanation: Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".
Example 2:

Input: s1 = "xy", s2 = "yx"
Output: 2
Explanation: Swap s1[0] and s2[0], s1 = "yy", s2 = "xx".
Swap s1[0] and s2[1], s1 = "xy", s2 = "xy".
Note that you cannot swap s1[0] and s1[1] to make s1 equal to "yx", cause we can only swap chars in different strings.
Example 3:

Input: s1 = "xx", s2 = "xy"
Output: -1
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1, s2 only contain 'x' or 'y'.
'''

########################################################################################################################################
# In this problem, we just need to find the count of different characters in both strings. 
# https://leetcode.com/problems/minimum-swaps-to-make-strings-equal/discuss/419874/Simply-Simple-Python-Solution-with-detailed-explanation
'''
Steps:
Get the count of "x_y" and "y_x"
If sum of both counts is odd then return -1. We need a pair to make the strings equal
Each 2 count of "x_y" needs just 1 swap. So add half of "x_y" count to the result
Each 2 count of "y_x" needs just 1 swap. So add half of "y_x" count to the result
if we still have 1 count of "x_y" and 1 count of "y_x" then they need 2 swaps so add 2 in result.
'''

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1
                    
        if (x_y + y_x) % 2 == 1:
            return -1
        # Both x_y and y_x count shall either be even or odd to get the result.
		# x_y + y_x should be even
        
        res = x_y // 2
        res += y_x // 2
        
        if x_y % 2 == 1:
            res += 2
        # If there count is odd i.e. we have "xy" and "yx" situation
        # so we need 2 more swaps to make them equal
            
        return res
        
