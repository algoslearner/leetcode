# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
'''
2128. Remove All Ones With Row and Column Flips

You are given an m x n binary matrix grid.

In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.

 

Example 1:


Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column
Example 2:


Input: grid = [[1,1,0],[0,0,0],[0,0,0]]
Output: false
Explanation: It is impossible to remove all 1's from grid.
Example 3:


Input: grid = [[0]]
Output: true
Explanation: There are no 1's in grid.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is either 0 or 1.
'''

#########################################################################################################################
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/discuss/1671908/Python-3-or-Math-or-Explanation
# TC: O(mn)
# SC: O(1)
'''
Explanation
I honestly don't know how to categorize this problem. It seems like a Math problem to me. Once you understand the logic, the implementation is simple.
Basically the "pattern" of each row should be the same, by pattern, I mean following:
  001100 and 001100 are the same pattern
  001100 and 110011 (the invert of original) are the same pattern
Only in above situation, one matrix can be converted to all zero

Intuition?
  Believe it or not, I draw a couple examples to test it out and suddenly it becomes obvious
  I guess it's good habit to get your hands dirty :)
''' 

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        r1 = grid[0]
        r1_invert = [1-val for val in grid[0]]
        for i in range(1, len(grid)):
            if grid[i] != r1 and grid[i] != r1_invert:
                return False
        return True
      
      
#########################################################################################################################
# xor
# TC: O(mn)
# SC: O(1)

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] ^ grid[0][j]) != (grid[i][0] ^ grid[0][0]):
                    return False
        return True
