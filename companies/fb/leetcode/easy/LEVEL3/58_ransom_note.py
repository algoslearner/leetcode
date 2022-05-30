# https://leetcode.com/problems/ransom-note/solution/
'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

############################################################################################
# TC: O(n.m)
# SC: O(1)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            if i in magazine:
                magazine = magazine.replace(i,"",1)
            else: return False
        
        return True
       
############################################################################################
# hashset
# TC: O(m)
# SC: O(1)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqmap = {}
        for c in magazine:
            if c in freqmap:
                freqmap[c] += 1
            else:
                freqmap[c] = 1
        
        for c in ransomNote:
            if c in freqmap:
                if freqmap[c] <= 0: return False
                freqmap[c] -= 1
            else:
                return False
            
        return True
