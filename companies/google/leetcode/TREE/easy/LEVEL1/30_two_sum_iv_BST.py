# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''
653. Two Sum IV - Input is a BST

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###############################################################################################
# INORDER TRAVERSAL + 2 pointers binary-search
# TC: O(n)
# SC: O(n)

class Solution:
    def inorder(self, root, output):
        if root == None:
            return
        else:
            self.inorder(root.left,output)
            output.append(root.val)
            self.inorder(root.right,output)
            
    def findTarget(self, root: TreeNode, k: int) -> bool:
        output = []
        self.inorder(root,output)
        l,r = 0 ,len(output) - 1
        while l < r:
            Sum = output[l] + output[r]
            if Sum == k:
                return True
            else:
                if Sum < k:
                    l += 1
                else:
                    r -= 1
        return False
       
# You can also achieve O(h) space if you use a BST Iterator for the min and max node of the tree. Runtime will still be O(n)
