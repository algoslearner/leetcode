# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
'''
515. Find Largest Value in Each Tree Row

Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: [1,3,9]
Example 2:

Input: root = [1,2,3]
Output: [1,3]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-231 <= Node.val <= 231 - 1
'''

########################################################################################
# DFS + recursion

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        def helper(root, depth, res):
            if not root:
                return
            
            if len(res) == depth:
                res.append(float("-inf"))
            
            res[depth] = max(res[depth], root.val)
            
            helper(root.left, depth+1, res)
            helper(root.right, depth+1, res)
    
        res = []
        helper(root, 0, res)
        return res
      
########################################################################################
# BFS naive

class Solution(object):
    def largestValues(self, root):       
        if not root:
            return []
        
        result = []
        q = deque()
        q.append(root)
        while q:
            level_len = len(q)
            maximum = float('-inf')
            for _ in range(level_len):
                node = q.popleft()
                maximum = max(maximum, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(maximum)
        return result
