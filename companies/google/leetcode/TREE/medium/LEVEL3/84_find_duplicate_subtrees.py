# https://leetcode.com/problems/find-duplicate-subtrees/
'''
652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
'''

############################################################################################################
# https://leetcode.com/problems/find-duplicate-subtrees/discuss/1571352/Python-solution-explained-in-two-steps-for-beginners
# TC: O(N)
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        hmap = {}
        
        def recurse(node, path):
            if node is None:
                return '#'
            
            path += ','.join([str(node.val), recurse(node.left, path), recurse(node.right, path)])
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
            return path
        
        recurse(root, '')
        #print(hmap) I SUGGEST YOU PRINT THIS - TO UNDERSTAND WHAT IS HAPPENING.
        return res
