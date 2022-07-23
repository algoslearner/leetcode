# https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/ 
'''
2077. Paths in Maze That Lead to Same Room

A maze consists of n rooms numbered from 1 to n, and some rooms are connected by corridors. 
You are given a 2D integer array corridors where corridors[i] = [room1i, room2i] indicates that there is a corridor connecting room1i and room2i, allowing a person in the maze to go from room1i to room2i and vice versa.

The designer of the maze wants to know how confusing the maze is. 
The confusion score of the maze is the number of different cycles of length 3.

For example, 1 → 2 → 3 → 1 is a cycle of length 3, but 1 → 2 → 3 → 4 and 1 → 2 → 3 → 2 → 1 are not.
Two cycles are considered to be different if one or more of the rooms visited in the first cycle is not in the second cycle.

Return the confusion score of the maze.

 

Example 1:


Input: n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]
Output: 2
Explanation:
One cycle of length 3 is 4 → 1 → 3 → 4, denoted in red.
Note that this is the same cycle as 3 → 4 → 1 → 3 or 1 → 3 → 4 → 1 because the rooms are the same.
Another cycle of length 3 is 1 → 2 → 4 → 1, denoted in blue.
Thus, there are two different cycles of length 3.
Example 2:


Input: n = 4, corridors = [[1,2],[3,4]]
Output: 0
Explanation:
There are no cycles of length 3.
 

Constraints:

2 <= n <= 1000
1 <= corridors.length <= 5 * 104
corridors[i].length == 2
1 <= room1i, room2i <= n
room1i != room2i
There are no duplicate corridors.
'''

#######################################################################################################################################
# https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/discuss/1717194/Python-3-or-DFS-or-Complexity-Analysis
# DFS + stack + set for graph
# TC:
# SC:

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        
        # initialize graph
        adj_list_graph = defaultdict(set)
        
        # build graph
        for a, b in corridors:
            adj_list_graph[a].add(b)
            adj_list_graph[b].add(a)
        
        # DFS traversal
        stack = [1]
        visited = set()
        count = 0
        
        while stack:
            curr = stack.pop()
            visited.add(curr)
            for nei in adj_list_graph[curr]:
                if nei not in visited:
                    stack.append(nei)
                    # graph[neigh] => neigh's neighbors // graph[curr] => current node's neighbors
                    tmpInter = adj_list_graph[nei].intersection(adj_list_graph[curr])
                    count += len(tmpInter)
        return count // 3
