# https://leetcode.com/problems/distribute-coins-in-binary-tree/
'''
979. Distribute Coins in Binary Tree

You are given the root of a binary tree with n nodes where each node in the tree has node.val coins. There are n coins in total throughout the whole tree.

In one move, we may choose two adjacent nodes and move one coin from one node to another. A move may be from parent to child, or from child to parent.

Return the minimum number of moves required to make every node have exactly one coin.

 

Example 1:


Input: root = [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:


Input: root = [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves]. Then, we move one coin from the root of the tree to the right child.
 

Constraints:

The number of nodes in the tree is n.
1 <= n <= 100
0 <= Node.val <= n
The sum of all Node.val is n.
'''

####################################################################################################
'''
# LOGIC
# I think the problem needs to state that the total amount of coins equals the total amount of nodes.

Below is the basic intuition behind this problem:

Root asks the left subtree, how much do you need or you've got extra? I'll give that/take it away to/from you via our direct edge, and pass it to right child, and if something remains, I'll take it.
Same question is asked to the right child.
Answer will be the sum of values(absolute) returned after the asked questions from the left(Left) and right(Right).
But what should the root return to its parent? It will return that how much does "his tree" need/has extra. That will be the signed sum of its Left+Right (question's answer) + same question asked to current root node.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

####################################################################################################
# DFS
# TC: O(n), n = number of nodes of tree
# SC: O(h), h = height of tree

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
