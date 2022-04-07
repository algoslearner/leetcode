'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#######################################################################################################
# RECURSION with range of valid values
# TC: O(N)
# SC: O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val <= low and node.val >= high:
                return False
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)
        
        return validate(root)
      
#######################################################################################################
# RECURSION inorder traversal
# TC: O(N)
# SC: O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)
        
        self.prev = -math.inf
        return inorder(root)
      
      
#######################################################################################################
# ITERATION inorder traversal
# TC: O(N)
# SC: O(N)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = -math.inf
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            # next element smaller than previous one
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right
        
        return True
