# https://leetcode.com/problems/find-the-town-judge/
'''
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''

####################################################################################################
# two arrays
# TC: O(max(E, N))
# SC: O(N)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # corner case
        if len(trust) < n - 1:
            return -1
        
        indegree = [0] * (n + 1)
        outdegree = [0] * (n + 1)
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
            
        for i in range(1, n + 1):
            if indegree[i] == n - 1 and outdegree[i] == 0:
                return i
        return -1
      
#####################################################################################################
# using one array
# TC: O(E)
# SC: O(N)

def findJudge(self, N: int, trust: List[List[int]]) -> int:

    if len(trust) < N - 1:
        return -1

    trust_scores = [0] * (N + 1)
    for a, b in trust:
        trust_scores[a] -= 1
        trust_scores[b] += 1
    
    for i, score in enumerate(trust_scores[1:], 1):
        if score == N - 1:
            return i
    return -1
