'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
 

Constraints:

1 <= num.length <= 50
num consists of only digits.
num does not contain any leading zeros except for zero itself.
'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # rotatable numbers : 0 1 6 8 9
        
        rotated_num = ""
        for n in reversed(num):
            if n == '0' or n == '1' or n == '8':
                rotated_num += n
            elif n == '6':
                rotated_num += '9'
            elif n == '9':
                rotated_num += '6'
            else:
                return False
        return num == rotated_num
