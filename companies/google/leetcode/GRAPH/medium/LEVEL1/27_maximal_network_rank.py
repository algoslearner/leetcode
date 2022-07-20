# https://leetcode.com/problems/maximal-network-rank/
'''
1615. Maximal Network Rank

There is an infrastructure of n cities with some number of roads connecting these cities. 
Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. 
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 

Example 1:



Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
Example 2:



Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
Output: 5
Explanation: There are 5 roads that are connected to cities 1 or 2.
Example 3:

Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
Output: 5
Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 

Constraints:

2 <= n <= 100
0 <= roads.length <= n * (n - 1) / 2
roads[i].length == 2
0 <= ai, bi <= n-1
ai != bi
Each pair of cities has at most one road connecting them.
'''

########################################################################################################################
# TC: O(N^2)
# SC: O(n)
# https://leetcode.com/problems/maximal-network-rank/discuss/891726/Python-Solution-using-Frequency-Array
'''
The Basic Idea is to Create 2 Counter Dictionaries, 
1.  One to store the number of roads emerging from each node and 
2.  the other to store all the pairs having roads in between them. 
So, any checking now takes O(1) time, making our overall solution O(N^2).

Now, we check every possible pair from 0 to N-1:
1.  If we found the pair having a road between them, we find the roads in O(1) by adding each of their roads and subtracting one for the common road we added twice.
2.  Else there is no road between them and we just add the roads each of the nodes lead to in O(1).
We just keep track of the maximum for all such pairs and return the value.
'''


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        roadcount = [0] * n
        c = Counter()
        for a, b in roads:
            roadcount[a] += 1
            roadcount[b] += 1
            c[(a, b)] = True
        
        rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                if c[(i, j)] or c[(j, i)]: 
                    curr = roadcount[i] + roadcount[j] - 1
                else:
                    curr = roadcount[i] + roadcount[j]
                rank = max(rank, curr)
        return rank
