# https://leetcode.com/problems/average-of-levels-in-binary-tree/
'''
637. Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

################################################################################################
# BFS
# TC: O(n)
# SC: O(n)

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        
        if not root:
            return []
        
        q = deque()
        q.append(root)
        while q:
            levelsize = len(q)
            curr_sum = 0
            for _ in range(levelsize):
                node = q.popleft()
                curr_sum += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            avg = curr_sum / levelsize
            result.append(avg)
        
        return result
      
      
 ###############################################################################################
# DFS
# TC: O(n)
# SC: O(n)

class Solution:
    def averageOfLevels(self, root):
        info = []
        def dfs(node, depth = 0):
            if node:
                if len(info) <= depth:
                    info.append([])
                info[depth].append(node.val)

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)
        
        dfs(root)
        return [sum(s)/len(s) for s in info]
