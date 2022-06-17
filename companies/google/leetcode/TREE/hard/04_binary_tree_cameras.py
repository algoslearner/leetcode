# https://leetcode.com/problems/binary-tree-cameras/
'''
968. Binary Tree Cameras

You are given the root of a binary tree. 
We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.

Return the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:


Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. 
The above image shows one of the valid configurations of camera placement.
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
Node.val == 0
'''

#######################################################################################################################
# DP
# TC: O(N)
# SC: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node:
                return 0, 0, float('inf')
            L = solve(node.left)
            R = solve(node.right)
            
            dp0 = L[1] + R[1]
            dp1 = min(L[2] + min(R[1:]),  R[2] + min(L[1:]))
            dp2 = 1 + min(L) + min(R)
            
            return dp0, dp1, dp2
        
        return min(solve(root)[1:])
       
##############################################################################################################################
# greedy
# TC: O(N)
# SC: O(H)

class Solution(object):
    def minCameraCover(self, root):
        self.ans = 0
        covered = {None}

        def dfs(node, par = None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (par is None and node not in covered or
                        node.left not in covered or node.right not in covered):
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans
