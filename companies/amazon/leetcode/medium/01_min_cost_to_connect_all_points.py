'''
1584. Min Cost to Connect All Points

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
'''

########################################################################################
# Minimum Spanning Tree
'''
We can say this problem is a variant of graph problems. 
More precisely, it is a Minimum Spanning Tree (MST) problem, 
where we are given nodes (points) and weighted edges (distance between two points) 
and we have to form an MST using them.
'''

########################################################################################
# Minimum Spanning Tree - Kruskal's Algorithm
# TC: O(N^2 log N)
# SC: O(N^2)

class UnionFind:
    def __init__(self, size: int) -> None:
        self.group = [0] * size
        self.rank = [0] * size
        
        for i in range(size):
            self.group[i] = i
      
    def find(self, node: int) -> int:
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]

    def join(self, node1: int, node2: int) -> bool:
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        # node1 and node2 already belong to same group.
        if group1 == group2:
            return False

        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group1] = group2
            self.rank[group2] += 1

        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        all_edges = []
        
        # Storing all edges of our complete graph.
        for curr_node in range(n): 
            for next_node in range(curr_node + 1, n): 
                weight = abs(points[curr_node][0] - points[next_node][0]) +\
                         abs(points[curr_node][1] - points[next_node][1])
                all_edges.append((weight, curr_node, next_node))
      
        
        # Sort all edges in increasing order.
        all_edges.sort()
        
        uf = UnionFind(n)
        mst_cost = 0
        edges_used = 0
        
        for weight, node1, node2 in all_edges:
            if uf.join(node1, node2):
                mst_cost += weight
                edges_used += 1
                if edges_used == n - 1:
                    break
        return mst_cost

########################################################################################
# Minimum Spanning Tree - Prim's Algorithm
# TC: O(N^2 log N)
# SC: O(N^2)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # Min-heap to store minimum weight edge at top.
        heap = [(0, 0)]
        
        # Track nodes which are included in MST.
        in_mst = [False] * n
        
        mst_cost = 0
        edges_used = 0
        
        while edges_used < n:
            weight, curr_node = heapq.heappop(heap)
            
            # If node was already included in MST we will discard this edge.
            if in_mst[curr_node]:
                continue
            
            in_mst[curr_node] = True
            mst_cost += weight
            edges_used += 1
            
            for next_node in range(n):
                # If next node is not in MST, then edge from curr node
                # to next node can be pushed in the priority queue.
                if not in_mst[next_node]:
                    next_weight = abs(points[curr_node][0] - points[next_node][0]) +\
                                  abs(points[curr_node][1] - points[next_node][1])
                    
                    heapq.heappush(heap, (next_weight, next_node))
                    
        return mst_cost

########################################################################################
# Minimum Spanning Tree - Prim's Algorithm (optimized)
# TC: O(N^2)
# SC: O(N)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_cost = 0
        edges_used = 0
        
        # Track nodes which are visited.
        in_mst = [False] * n
        
        min_dist = [math.inf] * n
        min_dist[0] = 0
        
        while edges_used < n:
            curr_min_edge = math.inf
            curr_node = -1
            
            # Pick least weight node which is not in MST.
            for node in range(n):
                if not in_mst[node] and curr_min_edge > min_dist[node]:
                    curr_min_edge = min_dist[node]
                    curr_node = node
            
            mst_cost += curr_min_edge
            edges_used += 1
            in_mst[curr_node] = True
            
            # Update adjacent nodes of current node.
            for next_node in range(n):
                weight = abs(points[curr_node][0] - points[next_node][0]) +\
                         abs(points[curr_node][1] - points[next_node][1])
                
                if not in_mst[next_node] and min_dist[next_node] > weight:
                    min_dist[next_node] = weight
        
        return mst_cost
