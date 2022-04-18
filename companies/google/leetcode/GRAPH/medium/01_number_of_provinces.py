'''
547. Number of Provinces
Google 2, Fb 5, Amazon 3

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
'''


# https://leetcode.com/problems/number-of-provinces/discuss/101349/Python-Simple-Explanation

############################################################################################################
# Recursion
# TC: O(n)
# SC: O(n)
# From some source, we can visit every connected node to it with a simple DFS. As is the case with DFS's, seen will keep track of nodes that have been visited.
# For every node, we can visit every node connected to it with this DFS, and increment our answer as that represents one friend circle (connected component.)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        A = isConnected
        N = len(A)
        seen = set()
        
        def dfs(node):
            for nei, adj in enumerate(A[node]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
                    
        ans = 0
        for i in range(N):
            if i not in seen:
                dfs(i)
                ans += 1
        return ans
  
############################################################################################################
# Iteration
# TC: O(n)
# SC: O(n)

 class Solution(object):
    def findCircleNum(self, M):
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    cur = toSee.pop()
                    if cur not in seen:
                        seen.add(cur)
                        toSee = [j for j,v in enumerate(M[cur]) if v and j not in seen] + toSee
                res += 1
        return res
