'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
'''

##############
'''
Simple Python3 solution using dict/hashtable. I like it because it's intuitive and the "step" between rows can be visualised. 76ms runtime (99.62th percentile).

try except block without specific error (KeyError to avoid string length < numRows) might be bad form but specifying strangely increased runtime considerably.
'''

# TC: O(n)
# SC: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        step = 1
        pos = 1
        
        lines = {}
        for c in s:
            if pos not in lines:
                lines[pos] = c
            else:
                lines[pos]+=c
            pos+=step
            if pos==1 or pos==numRows:
                step*=-1
        
        sol = ""
        for i in range(1, numRows+1):
            try:
                sol+=lines[i]
            except:
                return sol
        return sol
