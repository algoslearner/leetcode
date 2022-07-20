# 
'''
1319. Number of Operations to Make Network Connected

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network 
where connections[i] = [ai, bi] represents a connection between computers ai and bi. 
Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. 
You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
'''

#############################################################################################################################################
# DFS
# TC: O(connections)
# SC: O(n)
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/discuss/477679/Python-Count-the-Connected-Networks

'''
We need at least n - 1 cables to connect all nodes (like a tree).
If connections.size() < n - 1, we can directly return -1.

One trick is that, if we have enough cables,
we don't need to worry about where we can get the cable from.

We only need to count the number of connected networks.
To connect two unconneccted networks, we need to set one cable.

The number of operations we need = the number of connected networks - 1
'''

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: 
            return -1
        
        graph = [set() for i in range(n)]
        for a, b in connections:
            graph[a].add(b)
            graph[b].add(a)
            
        def dfs(i):
            if seen[i]: return 0
            seen[i] = 1
            for nei in graph[i]: dfs(nei)
            return 1
        
        seen = [0] * n
        return sum(dfs(i) for i in range(n)) - 1
      
#############################################################################################################################################
# union find
# TC: O(connections)
# SC: O(n)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        p = {}
        def find(x):
            p.setdefault(x, x)
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]
        
        def union(x, y):
            p[find(x)] = find(y)
            
        for a, b in connections:
            union(a, b)
            
        k, t = len(set(map(find, range(n)))) - 1, len(connections)
        r = t - (n - k - 1)
        return k if r >= k else -1
