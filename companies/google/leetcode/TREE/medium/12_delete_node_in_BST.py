'''
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?

'''

#####################################################################################################
# RECURSION
# TC: O(log N)
# SC: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def predecessor(self, root):
        # one step left and then always right
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def successor(self, root):
        # one step right and then always left
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            # delete from right subtree
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            # delete from left subtree
            root.left = self.deleteNode(root.left, key)
        else:
            # delete the current node
            if not (root.left or root.right):
                # node is a leaf
                root = None
            elif root.right:
                # node is not a leaf and has a right child
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:
                # node is not a leaf, no right child, but has a left child
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
                
