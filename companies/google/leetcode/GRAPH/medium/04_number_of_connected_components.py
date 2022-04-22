'''
323. Number of Connected Components in an Undirected Graph
Google 2, Fb 3, Amazon 6, Linkedin 4

You have a graph of n nodes. 
You are given an integer n and an array edges 
where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:


Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2
Example 2:


Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1
 

Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
There are no repeated edges.
'''

##############################################################################################################
# DISJOINT SET - UNION FIND
# TC : O(E. alpha(n))
# SC : O(V)

class UnionFind:
    def __init__(self, n: int) -> None:
        self.root = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n
        
    def find(self, x: int) -> int:
        if x == self.root[x]:
            return x
        
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.count -= 1
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
        
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(*edge)
            
        return uf.count     
##############################################################################################################
# DFS of graph
# TC : O(E + V)
# SC : O(E + V)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        graph = [[] for _ in range(n)]
        seen = [False for _ in range(n)]
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            for adj in graph[node]:
                if not seen[adj]:
                    seen[adj] = True
                    dfs(adj)
                    
        for i in range(n):
            if not seen[i]:
                count += 1
                seen[i] = True
                dfs(i)
                
        return count    
