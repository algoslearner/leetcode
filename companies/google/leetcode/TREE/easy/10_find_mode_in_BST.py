'''
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''

#######################################################################################################################################
# RECURSION
# TC: O(N)
# SC: O(N)

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        
        cnts = collections.Counter()
        mv = 0
        
        def helper(node):
            nonlocal mv
            if not node:
                return
            cnts[node.val] += 1
            mv = max(mv, cnts[node.val])
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return [k for k,v in cnts.items() if v == mv]

#######################################################################################################################################
# RECURSION
# TC: O(N)
# SC: O(1)
# Inorder traversal of a BST will find the nodes in ascending order. So just compare the current node to the previous, and if they match, increase the current count of duplicate values by 1. If they don't match, reset the current count to 1. Compare the current count to the max count found so far. If they match, append the current value to the result list. If the current count of duplicates exceeds the max count, create a new result list with just the current value.

class Solution(object):
    prev = None
    max_count = 0
    current_count = 0 
    result = []

    def findMode(self, root):
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if not node: return
        self.dfs(node.left)
        self.current_count = 1 if node.val != self.prev else self.current_count + 1
        if self.current_count == self.max_count:
            self.result.append(node.val)
        elif self.current_count > self.max_count:
            self.result = [node.val]
            self.max_count = self.current_count
        self.prev = node.val
        self.dfs(node.right)
