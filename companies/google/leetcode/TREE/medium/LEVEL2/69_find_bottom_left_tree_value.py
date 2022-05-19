# https://leetcode.com/problems/find-bottom-left-tree-value/
'''
513. Find Bottom Left Tree Value

Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''

##########################################################################################################
# DFS
'''
Doing BFS right-to-left means we can simply return the last node's value 
and don't have to keep track of the first node in the current row or even care about rows at all.

Inspired by @fallcreek's solution (not published) which uses two nested loops to go row by row 
but already had the right-to-left idea making it easier. I just took that further.
'''

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        for node in queue:
            # queue += filter(None, (node.right, node.left))
            if node.right:
                queue += [node.right]
            if node.left:
                queue += [node.left]
        return node.val
