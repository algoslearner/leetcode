'''
897. Increasing Order Search Tree
FB 2, Amazon 2

Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]
 

Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#############################################################################################
# inorder traversal
# TC : O(n)
# SC : O(h)

class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        ans = cur = TreeNode(None)
        for v in inorder(root):
            cur.right = TreeNode(v)
            cur = cur.right
        return ans.right

#############################################################################################
# re-linking
# TC : O(n)
# SC : O(h)

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                # track the left side first
                inorder(node.left)
                
                # update the new tree
                node.left = None
                self.cur.right = node
                self.cur = node
                
                # track the right side then
                inorder(node.right)

        # generate new tree: self.cur for update, ans for return the root
        self.cur = TreeNode(None)
        ans = self.cur
        inorder(root)
        return ans.right
        
