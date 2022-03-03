'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        
        # 0. base case, if the lengths of s and t are different, return False
        if len(s) != len(t):
            return False
        # 1. set up a hashmap with the counts of the letters in s
        hashmap = {}
        for letter in s:
            hashmap[letter] = hashmap.get(letter, 0) + 1
        # 2. check if the letters in t are in the hashmap, if not return False, remove once the letters cancel out
        for letter in t:
            if letter in hashmap:
                hashmap[letter] -= 1
                if hashmap[letter] == 0:
                    hashmap.pop(letter)
            else:
                return False
        # 3. return if the hashmap is blank
        return hashmap == {}
