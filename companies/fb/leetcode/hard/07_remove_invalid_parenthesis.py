'''
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return all the possible results. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
'''

# https://leetcode.com/problems/remove-invalid-parentheses/discuss/75057/44ms-Python-solution
# Time:
# Space: 

'''
Scan from left to right, make sure count["("]>=count[")"].
Then scan from right to left, make sure count["("]<=count[")"].
'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def helper(open_brace, close_brace, results, reverse):            
            count = {open_brace: 0, close_brace: 0}
            removed = 0
            for i in range(len(s)):
                c = s[-(i+1)] if reverse else s[i]
                if c == close_brace and count[open_brace] == count[close_brace]:
                    new_results = set()
                    for result in results:
                        if reverse:
                            r = range(len(result) - (i - removed + 1), len(result))
                        else:
                            r = range(i - removed + 1)
                
                        for j in r:
                            if result[j] == close_brace:
                                new_results.add(result[:j] + result[j + 1:])
                    results = new_results
                    removed += 1
                elif c in count:
                        count[c] += 1
            return results

        results = {s}
        results = helper("(", ")", results, False)
        results = helper(")", "(", results, True)
        return list(results)
