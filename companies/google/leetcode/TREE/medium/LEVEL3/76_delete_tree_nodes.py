# https://leetcode.com/problems/delete-tree-nodes/
'''
1273. Delete Tree Nodes

A tree rooted at node 0 is given as follows:

The number of nodes is nodes;
The value of the ith node is value[i];
The parent of the ith node is parent[i].
Remove every subtree whose sum of values of nodes is zero.

Return the number of the remaining nodes in the tree.

 

Example 1:


Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
Output: 2
Example 2:

Input: nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
Output: 6
 

Constraints:

1 <= nodes <= 104
parent.length == nodes
0 <= parent[i] <= nodes - 1
parent[0] == -1 which indicates that 0 is the root.
value.length == nodes
-105 <= value[i] <= 105
The given input is guaranteed to represent a valid tree.
'''

###########################################################################################
# DFS
# TC: O(N)
# SC: O(N)

# https://leetcode.com/problems/delete-tree-nodes/discuss/440829/JavaC%2B%2BPython-One-pass
# Build up the mapping of parent and its children.
# Recursively find the sum and the count of subtree.

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        sons = {i: set() for i in range(nodes)}
        for i, p in enumerate(parent):
            if i: sons[p].add(i)

        def dfs(x):
            total, count = value[x], 1
            for y in sons[x]:
                t, c = dfs(y)
                total += t
                count += c
            return total, count if total else 0
        return dfs(0)[1]
      
