# https://leetcode.com/problems/find-leaves-of-binary-tree/
'''
366. Find Leaves of Binary Tree
=
Given the root of a binary tree, collect a tree's nodes as if you were doing this:

Collect all the leaf nodes.
Remove all the leaf nodes.
Repeat until the tree is empty.
 

Example 1:


Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]
Explanation:
[[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers since per each level it does not matter the order on which elements are returned.
Example 2:

Input: root = [1]
Output: [[1]]
 

Constraints:

The number of nodes in the tree is in the range [1, 100].
-100 <= Node.val <= 100
'''

#######################################################################################
# DFS
# TC: O(n)
# SC: O(n)
'''
Here's a simple python DFS implementation used to populate a dictionary (key = index, values = list of nodes), O(N) space, O(N) time, beats 99%

The DFS recursively calculates the layer index by getting the maximum depth from the left and right subtrees of a given node, which is then used to populate the dictionary.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = collections.defaultdict(list)
        
        def dfs(node, layer):
            if not node: 
                return layer 
            left = dfs(node.left, layer)
            right = dfs(node.right, layer)
            layer = max(left, right)
            output[layer].append(node.val)
            return layer + 1
        
        dfs(root, 0)
        return output.values() 
