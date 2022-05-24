# https://leetcode.com/problems/binary-tree-coloring-game/
'''
1145. Binary Tree Coloring Game

Two players play a turn based game on a binary tree. We are given the root of this binary tree, and the number of nodes n in the tree. n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x. The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player. In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn. If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player. If it is possible to choose such a y to ensure you win the game, return true. If it is not possible, return false.

 

Example 1:


Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
Example 2:

Input: root = [1,2,3], n = 3, x = 1
Output: false
 

Constraints:

The number of nodes in the tree is n.
1 <= x <= n <= 100
n is odd.
1 <= Node.val <= n
All the values of the tree are unique.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#####################################################################################################
# https://leetcode.com/problems/binary-tree-coloring-game/discuss/350738/Easy-to-understand-for-everyone
# https://leetcode.com/problems/binary-tree-coloring-game/discuss/350570/JavaC%2B%2BPython-Simple-recursion-and-Follow-Up
# TC: O(N)
# SC: O(height)

'''
Count left and right children's nodes of the player 1's initial node with value x. Lets call countLeft and countRight.

if countLeft or countRight are bigger than n/2, player 2 chooses this child of the node and will win.
If countLeft + countRight + 1 is smaller than n/2, player 2 chooses the parent of the node and will win;
otherwise, player 2 has not chance to win.
'''

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return count(root) / 2 < max(max(c), n - sum(c) - 1)
