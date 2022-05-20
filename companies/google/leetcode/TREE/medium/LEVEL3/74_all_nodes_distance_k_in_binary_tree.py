# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
'''
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, 
return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

########################################################################################################
# annotate parent
# tc: O(n)
# sc: O(n)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == k:
                return [node.val for node, d in queue]
            
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))
                    
        return []
      
########################################################################################################
# percolate distance
# tc: O(n)
# sc: O(n)

class Solution(object):
    def distanceK(self, root, target, K):
        ans = []

        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        def dfs(node):
            if not node:
                return -1
            elif node is target:
                subtree_add(node, 0)
                return 1
            else:
                L, R = dfs(node.left), dfs(node.right)
                if L != -1:
                    if L == K: ans.append(node.val)
                    subtree_add(node.right, L + 1)
                    return L + 1
                elif R != -1:
                    if R == K: ans.append(node.val)
                    subtree_add(node.left, R + 1)
                    return R + 1
                else:
                    return -1

        # Add all nodes 'K - dist' from the node to answer.
        def subtree_add(node, dist):
            if not node:
                return
            elif dist == K:
                ans.append(node.val)
            else:
                subtree_add(node.left, dist + 1)
                subtree_add(node.right, dist + 1)

        dfs(root)
        return ans
      
 ########################################################################################################
# convert tree to graph and then do bfs
# tc: O(n)
# sc: O(n)

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143729/Python-DFS-and-BFS
'''
A recursive dfs funciton connect help to build up a map conn.
The key of map is node's val and the value of map is node's connected nodes' vals.
Then we do N times bfs search loop to find all nodes of distance K
'''

def distanceK(self, root, target, K):
    conn = collections.defaultdict(list)
    def connect(parent, child):
        # both parent and child are not empty
        if parent and child:
            # building an undirected graph representation, assign the
            # child value for the parent as the key and vice versa
            conn[parent.val].append(child.val)
            conn[child.val].append(parent.val)
        # in-order traversal
        if child.left: connect(child, child.left)
        if child.right: connect(child, child.right)
    # the initial parent node of the root is None
    connect(None, root)
    # start the breadth-first search from the target, hence the starting level is 0
    bfs = [target.val]
    seen = set(bfs)
    # all nodes at (k-1)th level must also be K steps away from the target node
    for i in range(K):
        # expand the list comprehension to strip away the complexity
        new_level = []
        for q_node_val in bfs:
            for connected_node_val in conn[q_node_val]:
                if connected_node_val not in seen:
                    new_level.append(connected_node_val)
        bfs = new_level
        # add all the values in bfs into seen
        seen |= set(bfs)
    return bfs
