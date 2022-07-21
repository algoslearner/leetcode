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
# Union FInd Class
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
       
##########################################
# kruskal's algorithm + heap
# TC: O(E log E)
# SC: O(E)

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                pq.append(edge)
        
        # Convert pq into a heap.
        heapq.heapify(pq)

        result = 0
        count = size - 1
        while pq and count > 0:
            edge = heapq.heappop(pq)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.cost
                count -= 1
        return result

class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
if __name__ == "__main__":
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    solution = Solution()
    print(f"points = {points}")
    print(f"Minimum Cost to Connect Points = {solution.minCostConnectPoints(points)}")
 
 '''
 Finished in 59 ms
points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
Minimum Cost to Connect Points = 20
'''

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
