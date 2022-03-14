'''
A string is a valid parentheses string (denoted VPS) if and only if it consists of "(" and ")" characters only, and:

It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example,  "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

 

Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length).

Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

 

Example 1:

Input: seq = "(()())"
Output: [0,1,1,1,1,0]
Example 2:

Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]
 

Constraints:

1 <= seq.size <= 10000
'''

################################################################################################################
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/358419/Confused-by-this-problem-I-was-too-%3A(-Here-is-how-it-became-crystal-clear...
'''
So what we need is a strategy to cut any stack in half while making sure that the resulting half-stacks are balanced VPS. There are many ways of doing that, but one of the easiest (and seemingly a very common) approach is the odd/even strategy:

Get the depth at every index of the string
Put all odd-depth parentheses in one group, and all even-depth in the other
Done.
NOTE: Using this solution, parentheses at the same depth are always in the same group, so you can ensure that the resulting groups are balanced VPS.
'''

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        groups = []
        depth = 0
        for c in seq:
            if c == '(':
                depth += 1
            groups.append(depth % 2)  # group determined through parity (odd/even?) of depth
            if c != '(':
                depth -=1
    
        return groups
