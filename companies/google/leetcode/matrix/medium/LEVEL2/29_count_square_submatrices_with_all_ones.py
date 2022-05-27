# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# google 9, amazon 4
'''
1277. Count Square Submatrices with All Ones

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''

##################################################################################################
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution
# TC; O(mn)
# SC: O(1)
'''
dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.

If A[i][j] == 0, no possible square.
If A[i][j] == 1,
we compare the size of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1].
min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that we can find.

For example:
1, 1, 1
1, 1, 1
1, 1, 1

dp[0][0] = 1
dp[1][1] = 2 (the square including A[1][1] can be square with element A[1][1] with size: 2 * 2, 1 * 1)
dp[2][2] = 3 (the square including A[2][2] can be square with element A[2][2] with size: 3 * 3, 2 * 2, 1 * 1)
hope it helps.

#####################
some clarity on the explanation:
'A' given matrix and 'dp' dynamic matrix we are building,

If A[i][j]=1 we claim dp[i][j] = min(dp[i-1],[j], dp[i][j-1], dp[i-1][j-1]) + 1
above holds true because,
Imagine you have a square of size k where (i,j) is in the right down corner of it.
Then dp[i-1][j] is at least of size k-1 (as a sub square) and the same is true for dp[i][j-1] and dp[i-1],[j-1]
therefore min(dp[i-1],[j], dp[i][j-1], dp[i-1][j-1]) is at least k-1.

// Given matrix
[
[1,0,1],
[1,1,0],
[1,1,0]
]

// DP matrix
we fill the first row and first column with zeros and a cell is zero if A[i][j] = 0 (as this can't make a square matrix at all)
for A[i][j]>0 case we use the dp relation A[i][j] += min(A[i - 1][j - 1], min(A[i - 1][j], A[i][j - 1]));

0 0 0 0
0 1 0 1
0 1 1 0
0 1 2 0

hope this helps.
'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        A = matrix
        for i in range(1, len(A)):
            for j in range(1, len(A[0])):
                A[i][j] *= min(A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]) + 1
        return sum(map(sum, A))

