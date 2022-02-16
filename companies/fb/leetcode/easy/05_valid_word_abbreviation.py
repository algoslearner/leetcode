'''
A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
Example 2:

Input: word = "apple", abbr = "a2e"
Output: false
Explanation: The word "apple" cannot be abbreviated as "a2e".
 

Constraints:

1 <= word.length <= 20
word consists of only lowercase English letters.
1 <= abbr.length <= 10
abbr consists of lowercase English letters and digits.
All the integers in abbr will fit in a 32-bit integer.
'''



'''
Walkthrough
We maintain two pointers, i pointing at word and j pointing at abbr.
There are only two scenarios:

j points to a letter. We compare the value i and j points to. If equal, we increment them. Otherwise, return False.
j points to a digit. We need to find out the complete number that j is pointing to, e.g. 123. Then we would increment i by 123. We know that next we will:
either break out of the while loop if i or j is too large
or we will return to scenario 1.
'''

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0 
        while j < len(abbr) and i < len(word): 
            if abbr[j].isalpha(): 
                if abbr[j] != word[i]: 
                    return False 
                i += 1 
                j += 1 
            else: 
                if abbr[j] == '0':  # to handle edge cases such as "01", which are invalid
                    return False 
                temp = 0 
                while j < len(abbr) and abbr[j].isdigit(): 
                    temp = temp * 10 + int(abbr[j]) 
                    j += 1 
                i += temp  
        
        return j == len(abbr) and i == len(word)
                
                
# https://leetcode.com/problems/valid-word-abbreviation/discuss/358543/Detailed-Explanation-Python-O(N)-Two-Pointer-Solution
# two pointers
# TC : O(N)
# SC : O(1)              
        
