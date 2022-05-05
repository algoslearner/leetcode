# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
'''
1644. Lowest Common Ancestor of a Binary Tree II

Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
Example 3:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
 

Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

##########################################################################################
# Key Things to be aware about the find LCA II:
# 1.  Two target nodes is not guaranteed to exist in the tree
# 2.  A node is considered as descendant of itself.

# So remember that:
# we cannot instantly return the node we found here because we don't know if all m and n exist in the tree!


##########################################################################################
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/discuss/934848/Python-BFS-and-DFS-methods
# DFS : The idea is simmilar with 236. First call l, r to finish the traversal of a tree and used self.countp， self.countq to check the two target nodes exsit in the tree.
# TC: O(n)
# SC: O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.existq = False
        self.existp = False
        ans = self.dfs(root, p, q)
        return ans if self.existq and self.existp else None
    
    def dfs(self, node, p, q):
        if not node:
            return None
        # traverse children
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        # postorder
        if node == p:
            self.existp = True
            return node
        if node == q:
            self.existq = True
            return node
        if left and right:
            return node
        return left or right
      
      
##########################################################################################
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/discuss/934848/Python-BFS-and-DFS-methods
# BFS : The idea is simmilar with 1257, first visit all the nodes and record their parents, then use a set to store all the parents of one node and traverse the next node's ancestors to find the first parent in the set. \
# TC: O(n)
# SC: O(n)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root.val:None}
        stack = [root]
        while stack:
            node = stack.pop(0)
            if node.left:
                parents[node.left.val] = node
                stack.append(node.left)
            if node.right:
                parents[node.right.val] = node
                stack.append(node.right)
        ancestors = set()
        if p.val not in parents or q.val not in parents: return None
        while p:
            ancestors.add(p.val)
            p = parents[p.val]
        while q and q.val not in ancestors:
            q = parents[q.val]
        return q
