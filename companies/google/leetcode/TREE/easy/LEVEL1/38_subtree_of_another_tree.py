# https://leetcode.com/problems/subtree-of-another-tree/
'''
572. Subtree of Another Tree
Fb 6, Google 5, Amazon 4

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#############################################################################################
# Brute force
# TC: O(s * t)
# SC: O(s)

# https://leetcode.com/problems/subtree-of-another-tree/discuss/102741/Python-Straightforward-with-Explanation-(O(ST)-and-O(S%2BT)-approaches)
# isMatch function: check if s and t match at the values of their roots, plus their subtrees match.

class Solution:
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        
        return (s.val == t.val and 
            self.isMatch(s.left, t.left) and 
            self.isMatch(s.right, t.right))
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatch(root, subRoot): return True
        if not root: return False
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
#############################################################################################
# use hash
# TC: O(n)
# SC: O(s)
# https://leetcode.com/problems/subtree-of-another-tree/discuss/1130997/Python-or-O(n)-or-super-easy-to-understand

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def hashify(node):
            if not node:
                return None
            key = (node.val, hashify(node.left), hashify(node.right))
            return memo.setdefault(key, len(memo))
        
        memo = {}
        hashify(s)
        
        return (t.val, hashify(t.left), hashify(t.right)) in memo
