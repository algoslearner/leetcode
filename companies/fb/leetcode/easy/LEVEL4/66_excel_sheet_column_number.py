'''
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
'''

# READ
# https://leetcode.com/problems/excel-sheet-column-number/solution/
'''
Approach 2: Left to Right
Intuition

Rather than scanning from right to left as described in Approach 1, we can also scan the title from left to right.

For example, if we want to get the decimal value of string "1337", we can iteratively find the result by scanning the string from left to right as follows:

'1' = 1
'13' = (1 x 10) + 3 = 13
'133' = (13 x 10) + 3 = 133
'1337' = (133 x 10) + 7 = 1337
Instead of base-10, we are dealing with base-26 number system. Based on the same idea, we can just replace 10s with 26s and convert alphabets to numbers.

For a title "LEET":

L = 12
E = (12 x 26) + 5 = 317
E = (317 x 26) + 5 = 8247
T = (8247 x 26) + 20 = 214442

In Approach 1, we have built a mapping of alphabets to numbers. 
There is another way to get the number value of a character without building an alphabet mapping. 

You can do this by converting a character to its ASCII value and subtracting ASCII value of character 'A' from that value. 
By doing so, you will get results from 0 (for A) to 25 (for Z). 

Since we are indexing from 1, we can just add 1 up to the result. 
This eliminates a loop where you create an alphabet to number mapping which was done in Approach 1.
'''

# TC: O(N)
# SC: O(1)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = result * 26
            result += (ord(columnTitle[i]) - ord('A') + 1)
        return result
