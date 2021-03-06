'''
Given two integer arrays preorder and inorder where 
preorder is the preorder traversal of a binary tree and 
inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
################################################################################################
# TC: O(N^2), preorder.pop(0) will cost you n and for n times its n^2.
# SC: O(N)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(bound=None):
            if not inorder or inorder[0] == bound: return None
            root = TreeNode(preorder.pop(0))
            root.left = helper(root.val)
            inorder.pop(0)
            root.right = helper(bound)
            return root
            
        return helper()        

################################################################################################
# TC: O(N), improved with dequeue
# SC: O(N)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder=deque(preorder)
        inorder=deque(inorder)
        
        def helper(bound=None):
            if not inorder or inorder[0] == bound: return None
            root = TreeNode(preorder.popleft())
            root.left = helper(root.val)
            inorder.popleft()
            root.right = helper(bound)
            return root
        
        return helper()
