'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
If you do a breadth-first search and visit the right children first, 
then the first time you encounter a new depth is 
when you have met the rightmost visible child.
Time, space : O(n)
'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        look_up = {}
        
        def dfs(node, depth):
            if not node:
                return
            look_up[depth] = node.val
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)
            
        dfs(root, 0)
            
        return list(look_up.values())
