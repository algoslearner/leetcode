# https://leetcode.com/discuss/interview-question/1469651/amazon-oa-optimization-time-complexity-space-complexity
'''
Grid Climbing: 

A grid with mrows and n columns is used to form a cluster of nodes. 
If a point in the grid has a value of 1, then it represents a node. 
Each node in the cluster has a level associated with it. 
A node located in the throw of the grid is a level inode. 

Here are the rules for creating a cluster: Every node at level /connects to all the nodes at level k where > i and
kis the first level after level i that contains at least 1 node. • 
When i reaches the last level in the grid, no more connections are possible. . 

Given such a grid, find the number of connections present in the cluster.

Example: gridOfNodes = [[1, 1, 1], [0, 1, 0], [0, 0, 0],[1,1, 0]] .
• Row 1 to row 2: o Each of the three nodes in the first row connects to the single node in the second row: 3 connections. Row 2 to row 4: There is no node in row 3 so it is skipped.
• The single node in the second row connects to each of the two nodes in the last row: 2 connections. There are a total of 3 + 2 = 5 connections. Function Description Complete the numberOfConnections function in the editor below. The function must return a integer denoting the number of connections.
'''

# Similar Leetcode problem https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

#Solution in python - any suggestions are welcome!
def gridOfNodes(self, intervals: list[list[int]]) -> int:
        connections = 0
        prevNodes = 1
        # print(len(intervals[0]))
        for i in range(len(intervals)):
            currNodeCount = 0
            for j in range(len(intervals[0])):
                if(intervals[i][j] == 1):
                    currNodeCount+= 1
            if i == 0:
                prevNodes = currNodeCount
                continue
            elif currNodeCount >= 1:
                connections += currNodeCount * prevNodes
            prevNodes = currNodeCount
        return connections
      
#Improvised-
import collections
class Solution:
    def gridOfNodes(self, intervals: list[list[int]]) -> int:
        connections = 0
        prevNodes = intervals[0].count(1)
        for interval in intervals[1:]:
            currNodeCount = interval.count(1)
            if currNodeCount >= 1:
                connections += currNodeCount * prevNodes
                prevNodes = currNodeCount
        return connections
