'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 

Follow up: Recursive solution is trivial, could you do it iteratively?
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

################################################################################################
# postorder = left, right, root
################################################################################################
# RECURSION

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.dfs(root, output)
        return output
    
    def dfs(self, root: Optional[TreeNode], output: List[int]) -> None:
        if root:
            self.dfs(root.left, output)
            self.dfs(root.right, output)
            output.append(root.val)
            
################################################################################################
# ITERATION

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        stack = [root]
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        
        return output[::-1]
      
################################################################################################
# EASIER RECURSION

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        else:
            return []
