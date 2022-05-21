# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
'''
958. Check Completeness of a Binary Tree

Given the root of a binary tree, determine if it is a complete binary tree.

In a complete binary tree, every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.
Example 2:


Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
1 <= Node.val <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

############################################################################################################
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/205682/JavaC%2B%2BPython-BFS-Solution-and-DFS-Soluiton
# BFS
# TC: O(N)
# SC: O(N)

'''
Use BFS to do a level order traversal,
add childrens to the bfs queue,
until we met the first empty node.

For a complete binary tree,
there should not be any node after we met an empty one.

##
Also you may want to return earlier.
We can stop the first while loop when met the first null child.
From then on there should not be any more child.
This optimisation help reduce half of operations.
'''

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])
      
############################################################################################################
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/discuss/205682/JavaC%2B%2BPython-BFS-Solution-and-DFS-Soluiton
# DFS
# TC: O(N)
# SC: O(N)

def isCompleteTree(self, root):
        def dfs(root):
            if not root: return 0
            l, r = dfs(root.left), dfs(root.right)
            if l & (l + 1) == 0 and l / 2 <= r <= l:
                return l + r + 1
            if r & (r + 1) == 0 and r <= l <= r * 2 + 1:
                return l + r + 1
            return -1
        return dfs(root) > 0
