# https://leetcode.com/problems/tree-diameter/
'''
1245. Tree Diameter

The diameter of a tree is the number of edges in the longest path in that tree.

There is an undirected tree of n nodes labeled from 0 to n - 1. 
You are given a 2D array edges where edges.length == n - 1 and 
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the tree.

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

#######################################################################################################

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

#######################################################################################################
# REVISION
'''
How about we build on our hardly gained knowledge and reuse past solutions?

Let's start with a simpler problem:

I. Diameter of binary tree
https://leetcode.com/problems/diameter-of-binary-tree/

The approach there is to calculate the heights of left and right subtrees and check if the diameter passes trough the current node. Since it's a binary tree, we only have two heights to compute:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def diameter(root: TreeNode):
            if not root:
                return 0

            left_d = diameter(root.left)
            right_d = diameter(root.right)

            self.max_d = max(self.max_d, left_d+right_d)

            return max(left_d, right_d) + 1

        diameter(root)
        return self.max_d
        
II. Diameter of N-ary Tree
Let's generalize this to solve https://leetcode.com/problems/diameter-of-n-ary-tree/

The difference resides in the number of children a node has. Instead of getting back the left and right values, we now have have n heights were n if the number of children.
To maximize that height, we need to focus on the two biggest values. If those aren't enough to make a new diameter, other heights won't cut it:

    def diameter(self, root: 'Node') -> int:
        def recurse(node):
            if not node:
                return 0
        
            max_1, max_2 = 0, 0
            for child in node.children:
                d = recurse(child)
                
                if max_1 < max_2:
                    max_1 = max(max_1, d)
                else:
                    max_2 = max(max_2, d)
                
            self.diameter = max(self.diameter, max_1 + max_2)

            return max(max_1, max_2) + 1

        self.diameter = 0
        recurse(root)
        return self.diameter
        
III. Graph valid tree
Finally, let's get back to our problem. What's the difference with the one we just solved? We're getting a list of edges instead of root. How about we transform the input to get a root?
So from the edges list, we build an adjacency list. But there's one problem left to tackle. Simple cycles.
A tree will have simple cycles, i.e. cycles between parent and children. While applying the same above algorithm, we just need to make sure to take care of those cycles.
To do so, when doing a DFS, a pass the parent node to subcalls.
This is actually the solution of https://leetcode.com/problems/graph-valid-tree/

IV. Combining everything
Now here's the final result:

    def treeDiameter(self, edges: List[List[int]]) -> int:
        
 '''
 
