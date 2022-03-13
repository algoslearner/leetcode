'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
'''

# https://leetcode.com/problems/palindrome-partitioning/discuss/1667786/Python-Simple-Recursion-oror-Detailed-Explanation-oror-Easy-to-Understand
########################################################################################
'''
traverse and check every prefix s[:i] of s
if prefix s[:i] is a palindrome, then process the left suffix s[i:] recursively
since the suffix s[i:] may repeat, the memory trick can save some time
'''
class Solution:   
    @cache  # the memory trick can save some time
    def partition(self, s: str)  -> List[List[str]]:
        
        if not s: return [[]]
  
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
      
#######################################################################################
# Easier code to read, with same logic

class Solution:   
    def partition(self, s: str)  -> List[List[str]]:
        if len(s) == 0: return [[]]      
        
        def loops(output, tmp, s):
            if len(s) == 0:
                output.append(list(tmp))
                return
            
            for i in range(1, len(s)+1):
                if s[:i] == s[:i][::-1]:
                    loops(output, tmp+[s[:i]], s[i:])
                    
        output = []
        loops(output, [], s)          
        return output
