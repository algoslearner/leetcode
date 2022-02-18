'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
'''

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        sizes = [0] #island number to size. island number 0 will always be of size 0
        
        def find(x, y):
            #do not consider outof range or any numbered islands (numbers are negative in grid)
            if x == R or x == -1 or y == C or y == -1 or grid[x][y] < 1:
                return 0
                
            grid[x][y] = -len(sizes) #numbering islands -1, -2, -3, ....
            return 1 + find(x+1, y) + find(x, y+1) + find(x-1, y) + find(x, y-1)
        
       
        #find all islands.
        for i in range(R): #TC: O(R*C)
            for j in range(C):
                if grid[i][j] != 1: continue
                    
                area = find(i, j)
                sizes.append(area)
                
           
        #find a 0 which connects 2 or more islands. sum up their value
        largest = max(sizes)
        for i in range(R):  #TC: O(R*C)
            for j in range(C):
                if grid[i][j] != 0: continue
                    
                diffIslands = set() #find all different islands. 
                
                #a '0' can be touching same island in all directions.
                #so navigate in all available directions of '0'. find what is the number in the grid
                #that number is island number only represented negatively. so multiply by -1
                diffIslands.add(-1*grid[min(R-1,i+1)][j])
                diffIslands.add(-1*grid[max(0,i-1)][j])
                diffIslands.add(-1*grid[i][min(C-1,j+1)])
                diffIslands.add(-1*grid[i][max(0,j-1)])
                
                #from sizes array sum all diffrent islands touching '0'. add 1 for current '0'
                s = sum([sizes[i] for i in diffIslands])
                largest = max(largest, 1+s)
               
        
        return largest
                        
        #TC: O(R*C) = O(N^2)    
        
