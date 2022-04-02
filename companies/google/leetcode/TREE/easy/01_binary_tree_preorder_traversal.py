'''
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,2,3]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

########################################################################################
# preorder = root, left, right
########################################################################################
# RECURSION

class Solution: 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.dfs(root, output)
        return output
    
    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)   

########################################################################################
# ITERATIVE

class Solution: 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = [root]
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                stack.append(root.right)
                stack.append(root.left)
        return output
