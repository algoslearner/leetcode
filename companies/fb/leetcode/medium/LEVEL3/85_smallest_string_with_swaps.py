'''
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
'''

# SOLUTION
# https://leetcode.com/problems/smallest-string-with-swaps/discuss/753004/Clean-Python-DFS-or-O(-n-log-n-)

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        d = defaultdict(list)
        for a,b in pairs:
            d[a].append(b)
            d[b].append(a)
        #
        def dfs(x,A):
            if x in d:
                A.append(x)
                for y in d.pop(x):
                    dfs(y,A)
        #
        s    = list(s)
        while d:
            x = next(iter(d))
            A = []
            dfs(x,A)
            A = sorted(A)
            B = sorted([ s[i] for i in A ])
            for i,b in enumerate(B):
                s[A[i]] = b
        return ''.join(s)
