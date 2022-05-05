# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
'''
1305. All Elements in Two Binary Search Trees

Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

 

Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]
Example 2:


Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]
 

Constraints:

The number of nodes in each tree is in the range [0, 5000].
-105 <= Node.val <= 105
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

###############################################################################################################
# RECURSIVE
# TC: O( n+m log(n+m))
# SC: O( n+m )

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def inorder(node: TreeNode):
            if node:
                return inorder(node.left) + [node.val] + inorder(node.right)
            else:
                return []
            
        return sorted(inorder(root1) + inorder(root2))
      
###############################################################################################################
# Iterative : one pass, linear time
# TC: O( n+m )
# SC: O( n+m )

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2, output = [], [], []
        
        while root1 or root2 or stack1 or stack2:
            # update both stacks
            # by going left till possible
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            # Add the smallest value into output,
            # pop it from the stack,
            # and then do one step right
            if not stack2 or stack1 and stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                output.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                output.append(root2.val)   
                root2 = root2.right

        return output
