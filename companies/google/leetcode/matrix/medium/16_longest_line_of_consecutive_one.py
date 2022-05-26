# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/
# google 5
'''
562. Longest Line of Consecutive One in Matrix

Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

 

Example 1:


Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3
Example 2:


Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
'''

################################################################################################################################
# https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/discuss/102275/Python-Simple-with-Explanation
# TC; O(mn)
# SC:
'''
We can separate the problem into two subproblems. 
1. The first subproblem is, given a 1 dimensional list of 0's and 1's, what is the longest chain of consecutive 1s? 
2. The second subproblem is to generate every line (row, column, diagonal, and anti-diagonal).

The first problem is common. We keep track of the number of 1's we've seen before. If we see a 1, we add to our count and update our answer. If we see a 0, we reset.
The second part is more complex. We can try to manipulate indices of the grid, but there is a trick. Each element in the grid belongs to exactly 4 lines: the r-th row, c-th column, (r+c)-th diagonal, and (r-c)-th anti-diagonal. We scan from left to right, top to bottom, adding each element's value to it's respective 4 groups. As we visited in reading order, our lines will be appended to in that order, which is suitable for our purposes.
'''

class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        def longestLine(self, A):
            if not A: return 0
            
        def score(line):
            ans = count = 0
            for x in line:
                if x:
                    count += 1
                    ans = max(ans, count)
                else:
                    count = 0
            return ans
            #return max(len(list(v)) if k else 0 for k, v in itertools.groupby(line))
        
        
        groups = defaultdict(list)
        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                groups[0, r] += [val]
                groups[1, c] += [val]
                groups[2, r+c] += [val]
                groups[3, r-c] += [val]
        
        return max(map(score, groups.values()))
