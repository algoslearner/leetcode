# Amazon OA assignment: https://leetcode.com/discuss/interview-question/1033264/Amazon-or-OA-or-1-year-Experienced-for-SDE1

'''
Amazon Fresh Deliveries
Given allLocations list of co-ordinates (x,y) you have to find the X - closest locations from truck's location which is (0,0). Distance is calculated using formula (x^2 + y^2).
If the there is tie then choose the co-ordinate with least x value.
Sample Input :
allLocations : [ [1, 2] , [1, -1], [3, 4] ]
numOfDeliveries : 2
Sample Output :
[ [1, -1], [1 , 2] ]
Output list can be in any order.
This question was basically K closest points to the origin (0,0) with added tie condition.

Demolition Robot
Given a matrix with values 0 (trenches) , 1 (flat) , and 9 (obstacle) you have to find minimum distance to reach 9 (obstacle). If not possible then return -1.
The demolition robot must start at the top left corner of the matrix, which is always flat, and can move on block up, down, right, left.
The demolition robot cannot enter 0 trenches and cannot leave the matrix.
Sample Input :
[1, 0, 0],
[1, 0, 0],
[1, 9, 1]]
Sample Output :
3
This question can be solved by using BFS or DFS.
'''
