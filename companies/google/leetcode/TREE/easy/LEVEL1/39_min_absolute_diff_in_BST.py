# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
'''
530. Minimum Absolute Difference in BST

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 

Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
 

Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

####################################################################
# Inorder traversal
# TC: O(n)
# SC: O(n)

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        output = []
        self.inorder(root,output)
        mini_diff = float('inf')
        for i in range(1,len(output)):
            mini_diff = min(mini_diff,output[i]-output[i-1])
        return mini_diff
        
    def inorder(self,root,output):
        if root == None:
            return 
        else:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)
