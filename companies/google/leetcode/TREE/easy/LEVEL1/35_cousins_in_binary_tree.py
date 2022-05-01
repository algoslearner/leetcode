# https://leetcode.com/problems/cousins-in-binary-tree/
'''
993. Cousins in Binary Tree

Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:


Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Constraints:

The number of nodes in the tree is in the range [2, 100].
1 <= Node.val <= 100
Each node has a unique value.
x != y
x and y are exist in the tree.
'''

# https://leetcode.com/problems/cousins-in-binary-tree/discuss/654172/Python-Straight-Forward-BFS-and-DFS-Solutions
'''
Two solutions have the same idea:

Iterate the whole tree looking for the target(x and y) - either BFS or DFS
once found, store (parent, depth) as a tuple
Compare the parents and depth of two nodes found and get result
'''

################################################################################################
# DFS

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		# store (parent, depth) tuple
		    res = [] 
        
		# dfs
        def dfs(node, parent, depth):
            if not node:
                return
            if node.val == x or node.val == y:
                res.append((parent, depth))
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
            
        dfs(root, None, 0)

		# unpack two nodes found
        node_x, node_y = res  
		
		# compare and decide whether two nodes are cousins
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]
    
################################################################################################
# BFS

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
		# store (parent, depth) tuple
        res = []
		
		# bfs
        queue = deque([(root, None, 0)])        
        while queue:
			# minor optimization to stop early if both targets found
            if len(res) == 2:
                break
            node, parent, depth = queue.popleft()
            # if target found
            if node.val == x or node.val == y:
                res.append((parent, depth))
            if node.left:
                queue.append((node.left, node, depth + 1))
            if node.right:
                queue.append((node.right, node, depth + 1))

		# unpack two nodes
        node_x, node_y = res
		
		# compare and decide whether two nodes are cousins		
        return node_x[0] != node_y[0] and node_x[1] == node_y[1]

