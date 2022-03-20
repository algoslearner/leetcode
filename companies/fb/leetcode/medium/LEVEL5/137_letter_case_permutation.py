'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]
 

Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
'''

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        output = [""]
        
        for c in S:
            tmp = []
            if c.isalpha():
                for o in output:
                    tmp.append(o + c.lower())
                    tmp.append(o + c.upper())
            else:
                for o in output:
                    tmp.append(o + c)
            output = tmp
        
        return output
      
      
# Total combinations of such strings are 2^n - 
# where n is the number of alphabet chars, because every char can be in 2 states (lower and upper). So, inner loop complexity should be O(2^n).

# Time complexity = O(n * 2^n)
# Space complexity = O(n)
# tutorial followed: https://www.youtube.com/watch?v=_Ipng-tBpSw
