'''
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
 

Constraints:

1 <= s.length, goal.length <= 2 * 104
s and goal consist of lowercase letters.
'''

# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/92955/Python-4-lines-with-short-explanation
'''
Explanation
If A.length() != B.length(): no possible swap

If A == B, we need swap two same characters. Check is duplicated char in A.

In other cases, we find index for A[i] != B[i]. There should be only 2 diffs and it's our one swap.
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # enumerate cases
        # TC: O(N)
        # SC : O(1)
        
        if len(s) != len(goal): return False
        if s == goal and len(set(s)) < len(s): return True
        
        dif = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]

       
 #################################################################################
 '''
 I solved it following way.
#1 - if both strings length not matching, return false
#2 - if both strings are equal, but have any character repeating more than once, its swappable so return true
#3 - if more than 2 diffs, it won't match by swapping twice, so return false
#4 - When the diff is exactly two, for it to be swappable, the sorted values of both diffs should match up and return true, else false.
'''
 
 class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal): 
            return False
        
        if s == goal:
            seen = set()
            for a in s:
                if a in seen:
                    return True
                seen.add(a)
            return False

        pairs = []
        for a, b in zip(s, goal):
            if a != b:
                pairs.append((a, b))
            if len(pairs) >= 3: 
                return False
        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]
