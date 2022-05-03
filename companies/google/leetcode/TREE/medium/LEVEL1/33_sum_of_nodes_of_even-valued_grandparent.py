# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
'''
1315. Sum of Nodes with Even-Valued Grandparent

Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###########################################################################################################
# DFS - recursion
# TC: O(n)
# SC: O(n)

class Solution:
    def sumOfNodes(self, curr: TreeNode, p: TreeNode, gp: TreeNode) -> int:
        if not curr:
            return 0
        result = 0
        if gp and gp.val % 2 == 0:
            result += curr.val
        return result + self.sumOfNodes(curr.left, curr, p) + self.sumOfNodes(curr.right, curr, p)
        
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        result = 0
        result = self.sumOfNodes(root, None, None)
        return result
