# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
'''
1022. Sum of Root To Leaf Binary Numbers

You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val is 0 or 1.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##########################################################################################
# DFS Preorder traversal
# Recursive - simplest to write
# TC: O(N)
# SC: O(H)

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preorder(node, curr_num):
            nonlocal sum_root_to_leaf
            if node:
                curr_num = (curr_num << 1) | node.val
                # if its a leaf, update the sum
                if not (node.left or node.right):
                    sum_root_to_leaf += curr_num
                
                preorder(node.left, curr_num)
                preorder(node.right, curr_num)
            
        sum_root_to_leaf = 0
        preorder(root, 0)
        return sum_root_to_leaf

##########################################################################################
# DFS Preorder traversal
# Iteration - best time
# TC: O(N)
# SC: O(H)

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = 0
        stack = [(root, 0) ]
        
        while stack:
            node, curr_num = stack.pop()
            if node:
                curr_num = (curr_num << 1) | node.val
                # if it's a leaf, update root-to-leaf sum
                if node.left is None and node.right is None:
                    root_to_leaf += curr_num
                else:
                    stack.append((node.right, curr_num))
                    stack.append((node.left, curr_num))
                        
        return root_to_leaf
      
##########################################################################################
# DFS Preorder traversal
# Morris - contsant space, two pass
# TC: O(N)
# SC: O(1)

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        root_to_leaf = curr_number = 0
        
        while root:  
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left: 
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left 
                steps = 1
                while predecessor.right and predecessor.right is not root: 
                    predecessor = predecessor.right 
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val                    
                    predecessor.right = root  
                    root = root.left  
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number >>= 1
                    predecessor.right = None
                    root = root.right 
                    
            # If there is no left child
            # then just go right.        
            else: 
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right
                        
        return root_to_leaf
