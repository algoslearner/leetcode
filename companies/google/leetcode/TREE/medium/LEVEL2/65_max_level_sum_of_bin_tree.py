# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
'''
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
'''

#######################################################################################################################
# DFS + preorder recursive
# TC: O(N)
# SC: O(1)

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        def inorder(node, level):
            if node:
                inorder(node.left, level + 1)
                level_sum[level] += node.val
                inorder(node.right, level + 1)
            
        level_sum = defaultdict(int)
        inorder(root, 1)
        
        # Choose the level with the greatest sum "level_sum[level]" and if
        # there is a tie, then select the smaller level "-level".
        return max(level_sum, key=lambda level : (level_sum[level], -level))
      
      
#######################################################################################################################
# BFS + recursion
# TC: O(N)
# SC: O(N)

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        curr_level = max_level = 1
        max_sum = float('-inf')
        queue = [root, ]
        
        while queue:
            # sum up all the nodes on the current level
            curr_sum = sum([x.val for x in queue])
            # update max_sum 
            if curr_sum > max_sum:
                max_sum, max_level = curr_sum, curr_level
            # build next level
            queue = [y for x in queue for y in [x.left, x.right] if y]
            curr_level += 1
            
        return max_level
