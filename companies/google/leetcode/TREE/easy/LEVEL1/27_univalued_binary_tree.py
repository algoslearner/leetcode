# https://leetcode.com/problems/univalued-binary-tree/
'''
965. Univalued Binary Tree

A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

 

Example 1:


Input: root = [1,1,1,1,1,null,1]
Output: true
Example 2:


Input: root = [2,2,2,5,2]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
0 <= Node.val < 100
'''

###################################################################################
# DFS
# TC: O(n)
# SC: O(n)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        vals = []
        
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(set(vals)) == 1
      
###################################################################################
# RECURSION
# TC: O(n)
# SC: O(n)

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if root.left:
            if root.val != root.left.val: return False
        if root.right:
            if root.val != root.right.val: return False
            
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
