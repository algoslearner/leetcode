'''
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108

'''


############################################################################
# Iterate the list of digits backwards and keep tracking of the max digit, as well as the digit that is smaller than the max.
# TC: O(n)
# SC: O(1)

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        p, q, max_i = -1, -1, len(digits)-1
        
        for i in range(max_i-1, -1, -1):
            if digits[i] > digits[max_i]:
                max_i = i
            elif digits[i] < digits[max_i]:
                p, q = i, max_i

        # swap
        if p > -1:
            digits[p], digits[q] = digits[q], digits[p]
            
        return int(''.join(digits))
                
