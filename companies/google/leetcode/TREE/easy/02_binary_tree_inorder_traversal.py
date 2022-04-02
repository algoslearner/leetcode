'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
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

#############################################################################################
# inorder = left, root, right
#############################################################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#############################################################################################
# RECURSION

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.dfs(root, output)
        return output
    
    def dfs(self, root: Optional[TreeNode], res: List[int]) -> None:
         if root:
            self.dfs(root.left, res)
            res.append(root.val)
            self.dfs(root.right, res)
            
#############################################################################################
# ITERATION

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmpNode = stack.pop()
                output.append(tmpNode.val)
                root = tmpNode.right

        return output
