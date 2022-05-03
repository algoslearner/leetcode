# https://leetcode.com/problems/clone-n-ary-tree/
'''
1490. Clone N-ary Tree

Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

class Node {
    public int val;
    public List<Node> children;
}
Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
 

Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 104].
 

Follow up: Can your solution work for the graph problem?

Clone directed graph: https://leetcode.com/problems/clone-n-ary-tree/
Clone un-directed graph: https://leetcode.com/problems/clone-graph/
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

#################################################################################################
# RECURSION (DFS)
# TC: O(n)
# SC: O(n)

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # base case
        if not root:
            return root
        
        node_copy = Node(root.val)
        for c in root.children:
            node_copy.children.append(self.cloneTree(c))
        
        return node_copy
      
#################################################################################################
# Iterative (DFS)
# TC: O(n)
# SC: O(n)

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':

        if not root:
            return root

        new_root = Node(root.val)
        # Starting point to kick off the DFS visits.
        stack = [(root, new_root)]

        while stack:
            old_node, new_node = stack.pop()
            for child_node in old_node.children:
                new_child_node = Node(child_node.val)

                # Make a copy for each child node.
                new_node.children.append(new_child_node)

                # Schedule a visit to copy the child nodes of each child node.
                stack.append((child_node, new_child_node))

        return new_root
