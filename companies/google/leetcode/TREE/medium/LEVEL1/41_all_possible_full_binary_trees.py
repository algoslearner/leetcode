# https://leetcode.com/problems/all-possible-full-binary-trees/
'''
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

Example 1:


Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Input: n = 3
Output: [[0,0,0]]
 

Constraints:

1 <= n <= 20
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###############################################################################################################
# Recursive
# TC: O(2^n)
# SC: O(2^n)

class Solution:
    def __init__(self):
        self.memo = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            ans = []
            for i in range(n):
                balance = n - 1 - i
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(balance):
                        bns = TreeNode(0)
                        bns.left = left
                        bns.right = right
                        ans.append(bns)
            
            self.memo[n] = ans
            
        return self.memo[n]
        
