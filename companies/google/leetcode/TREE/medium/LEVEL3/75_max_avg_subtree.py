# https://leetcode.com/problems/maximum-average-subtree/
'''
1120. Maximum Average Subtree

Given the root of a binary tree, return the maximum average value of a subtree of that tree. Answers within 10-5 of the actual answer will be accepted.

A subtree of a tree is any node of that tree plus all its descendants.

The average value of a tree is the sum of its values, divided by the number of nodes.

 

Example 1:


Input: root = [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have an average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have an average of 6 / 1 = 6.
For the node with value = 1 we have an average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
Example 2:

Input: root = [0,null,1]
Output: 1.00000
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 105
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

##############################################################################################
# simple DFS
# TC: O(N)
# SC: O(N)

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if not root:
            return 0
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            sum_left, nodes_left = dfs(node.left)
            sum_right, nodes_right = dfs(node.right)
            
            total_sum = node.val + sum_left + sum_right
            total_nodes = 1 + nodes_left + nodes_right
            avg = total_sum / total_nodes
            self.max_avg = max(self.max_avg, avg)
            
            return (total_sum, total_nodes)
        
        self.max_avg = float("-inf")
        dfs(root)
        return self.max_avg
            
