# https://leetcode.com/problems/closest-binary-search-tree-value/
'''
270. Closest Binary Search Tree Value
Fb 20

Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

 

Example 1:


Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 109
-109 <= target <= 109
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###################################################################################################
# recursive inorder traversal + linear search
# TC: O(n)
# SC: O(n)

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        def inorder(node):
            if node:
                return inorder(node.left) + [node.val] + inorder(node.right)
            else:
                return []
            
        return min(inorder(root), key = lambda x: abs(target - x))
      
###################################################################################################
# iterative inorder traversal + linear search
# TC: O(h + k)
# SC: O(h) 

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack, pred = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if pred <= target and target < root.val:
                return min(pred, root.val, key = lambda x: abs(target - x))
                
            pred = root.val
            root = root.right

        return pred
      
###################################################################################################
# binary search
# TC: O(h)
# SC: O(1) 

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val
        while root:
            closest = min(root.val, closest, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest
