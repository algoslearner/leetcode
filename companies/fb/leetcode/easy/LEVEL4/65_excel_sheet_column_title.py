'''
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 231 - 1
'''

# READ: https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation
# We can use (n-1)%26 instead, then we get a number range from 0 to 25.

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)

# Conversion from 10-ary numbers to 26-ary numbers. The tricky part is the lack of the equivalent number '0' in the 26-ary system.
# Easier logic, but slower in runtime

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber
        while n > 0:
            n -= 1  # 26 -> "Z"
            res += chr(n % 26 + ord('A'))
            n //= 26
        return res[::-1]

