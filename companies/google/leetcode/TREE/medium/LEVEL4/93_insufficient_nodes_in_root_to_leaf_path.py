# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
'''
1080. Insufficient Nodes in Root to Leaf Paths

Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
-105 <= Node.val <= 105
-109 <= limit <= 109
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

########################################################################################################
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/discuss/308326/JavaC%2B%2BPython-Easy-and-Concise-Recursion
# TC : O(N)
# SC : O(height) for recursion management.
'''
Intuition
If root is leaf,
we compare the limit and root.val,
and return the result directly.

If root is leaf,
we recursively call the function on root's children with limit = limit - root.val.

Note that if a node become a new leaf,
it means it has no valid path leading to an original leaf,
we need to remove it.
'''

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return root
        
        # case 1 : node is leaf
        if root.left is None and root.right is None:
            if root.val < limit: 
                return None
            else:
                return root
              
        # case 2 : node is not a leaf
        else:
            root.left = self.sufficientSubset(root.left, limit - root.val)
            root.right = self.sufficientSubset(root.right, limit - root.val)
            
            # all path from this node to leaf is insufficient
            if root.left is None and root.right is None:
                return None
            else:
                return root

