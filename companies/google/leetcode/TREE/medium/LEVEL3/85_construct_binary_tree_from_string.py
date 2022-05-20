# https://leetcode.com/problems/construct-binary-tree-from-string/
'''
536. Construct Binary Tree from String

You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

 

Example 1:


Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]
Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]
Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
 

Constraints:

0 <= s.length <= 3 * 104
s consists of digits, '(', ')', and '-' only.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
###############################################################################################
# simplified recursion

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        idx = 0
        
        def create(s):
            nonlocal idx
            if idx >= len(s):
                return None
            
            if s[idx] == ')':
                idx += 1
                return None
            # extract number ####
            sign = 1
            if s[idx] == '-':
                sign = -1
                idx += 1
            num = 0
            while idx < len(s) and s[idx] not in ['(',')']:
                num = num * 10 + int(s[idx])
                idx += 1
            # extract number complete ####
            root = TreeNode(num*sign)
            
            if idx < len(s) and s[idx] == '(':
                idx += 1
                root.left = create(s)
            
            if idx < len(s) and s[idx] == '(':
                idx += 1
                root.right = create(s)
            
            idx += 1
            
            return root
                
        return create(s)
