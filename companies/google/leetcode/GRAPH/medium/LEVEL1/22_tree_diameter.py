# https://leetcode.com/problems/tree-diameter/
'''
1245. Tree Diameter

The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. You are given a 2D array edges where edges.length == n - 1 and edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

Return the diameter of the tree.

 

Example 1:


Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: The longest path of the tree is the path 1 - 0 - 2.
Example 2:


Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

n == edges.length + 1
1 <= n <= 104
0 <= ai, bi < n
ai != bi
'''

###################################################################################################################################################
# TC:
# SC:

class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        tree = {n: [] for n in range(len(edges) + 1)}
        for e1, e2 in edges:
            tree[e1].append(e2)
            tree[e2].append(e1)
        
        def recurse(node, parent):
            max_1, max_2 = 0, 0
            for nei in tree.get(node):
                if nei == parent:
                    continue
                    
                d = recurse(nei, node)
                if max_1 < max_2:
                    max_1 = max(max_1, d)
                else:
                    max_2 = max(max_2, d)
                    
            self.diameter = max(self.diameter, max_1 + max_2)
            return max(max_1, max_2) + 1
        
        self.diameter = 0
        recurse(0, None)
        return self.diameter
