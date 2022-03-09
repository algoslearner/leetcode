'''
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

# In-built function
# TC: O(N)
# SC: O(N)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s or s.isspace():
            return 0
        else:
            return len(s.split()[-1])
          
          
# string index manipulation
# TC: O(N)
# SC; O(1)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim the trailing spaces
        p = len(s) - 1
        while p >= 0 and s[p] == ' ':
            p -= 1

        # compute the length of last word
        length = 0
        while p >= 0 and s[p] != ' ':
            p -= 1
            length += 1
        return length
