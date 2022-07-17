#
'''
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

##################################################################################################################################
# TC: O(nk)
# SC: O(1)
# https://leetcode.com/problems/subtree-of-another-tree/discuss/156321/Python-dfs-both-tree-at-same-time

'''
First, travel down the bigger tree via standard dfs, if we find node equal to the value of root of the smaller tree, compare the subtrees.

We travel down both subtrees at the same time and if and only if every node is the same then we know we have found the right subtree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, a: TreeNode, b: TreeNode) -> bool:
        if not b:
            return True
        
        def checkTree(root1, root2):
            if not root1 and not root2:
                return True
            elif root1 and not root2 or root2 and not root1:
                return False
            
            if root1.val != root2.val:
                return False
            
            return checkTree(root1.left, root2.left) and checkTree(root1.right, root2.right)
        
        def dfs(s, t):
            if not s:
                return False
             
            if s.val == t.val and checkTree(s, t):
                return True
            
            return dfs(s.left, t) or dfs(s.right, t)
            
        return dfs(a, b)
        

