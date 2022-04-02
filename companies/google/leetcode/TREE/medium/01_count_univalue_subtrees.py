'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

 

Example 1:


Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
 

Constraints:

The number of the node in the tree will be in the range [0, 1000].
-1000 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# bottom-up, first check the leaf nodes and count them, 
# then go up, if both children are "True" and root.val is equal to both children's values if exist, then root node is uniValue suntree node.

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.checkUni(root)
        return self.count

    def checkUni(self, root):
        if not root:
            return True
        
        l, r = self.checkUni(root.left), self.checkUni(root.right)
        if l and r and (not root.left or root.left.val == root.val) \
        and (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        
        return False
