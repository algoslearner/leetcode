# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
'''
1443. Minimum Time to Collect All Apples in a Tree

Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

 

Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 2:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
 

Constraints:

1 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
fromi < toi
hasApple.length == n
'''

###################################################################################################################
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/624141/Clean-Python-3-peel-onion-in-O(N)-100-timespace
# GRAPH

'''
Just like performing Kahn's algorithm of topological sort on a tree.
Sum degrees of each node first, then peel the tree from those nodes whose degree is 1.
Once there is no appropriate node can be removed, just return sum of all degrees.
Note that we shouldn't peel node 0 so let hasApple[0] = True at beginning.
Time: O(N)
Each edge will be visited at most twice, and there will be n - 1 edges because it's a tree.
Space: O(N)
'''

import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        hasApple[0], degree = True, [0] * n
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        queue = collections.deque(v for v in range(n) if degree[v] == 1)
        while queue:
            u = queue.popleft()
            if hasApple[u]: continue
            for v in graph[u]:
                if degree[v] > 0:
                    degree[v] -= 1
                    degree[u] -= 1
                    if degree[v] == 1:
                        queue.append(v)
        return sum(degree)
      
###################################################################################################################
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/discuss/624141/Clean-Python-3-peel-onion-in-O(N)-100-timespace
# GRAPH - 2

import collections
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node: int, prev: int) -> bool:
            for neighbor in graph[node]:
                if neighbor != prev and dfs(neighbor, node):
                    hasApple[node] = True
            return hasApple[node]

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dfs(0, -1)
        return (sum(hasApple) - hasApple[0]) * 2
