##############################################################################################################################
# Amazon OA question: https://leetcode.com/discuss/interview-question/1954928/Amazon-OA

##############################################################################################################################
# Similar Leetcode question: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

'''
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

 

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
Example 2:

Input: s = "ABA"
Output: 8
Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
Example 3:

Input: s = "LEETCODE"
Output: 92
 

Constraints:

1 <= s.length <= 105
s consists of uppercase English letters only.
'''

##############################################################################################################################
# USING ARRAY : https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1971127/Short-Python
# TC: O(n)
# SC: O(n)

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        indexes = defaultdict(list)
        for i, c in enumerate(s):
            indexes[c].append(i)
        
        result = 0
        for c in indexes:
            indexes[c] = [-1] + indexes[c] + [len(s)]
            for i in range(len(indexes[c]) - 2):
                r = indexes[c][i:i + 3]
                result += (r[1] - r[0]) * (r[2] - r[1])
        return result

##############################################################################################################################
# HASHMAP : https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/discuss/1823865/Very-Easy-to-understand-Dict-Solution-O(n)
# TC: O(n)
# SC: O(n)

class Solution:
  def uniqueLetterString(self, s: str) -> int:
    hashMap = {}   # {char: [positions]}
    for i in range(len(s)):
        char = s[i]
        if char in hashMap:
            hashMap[char].append(i)
        else:
            hashMap[char] = [-1]
            hashMap[char].append(i)
            
    count = 0
    for key in hashMap:
        positions = hashMap[key]
        
        positions.append(len(s))
        for i in range(1, len(positions) - 1):
            count = count + (positions[i] - positions[i-1]) * (positions[i+1] - positions[i])
    return count
