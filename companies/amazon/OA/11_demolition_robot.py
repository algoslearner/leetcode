# Amazon OA assignment: https://leetcode.com/discuss/interview-question/1033264/Amazon-or-OA-or-1-year-Experienced-for-SDE1

'''
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

# https://leetcode.com/discuss/interview-question/1257344/Amazon-OA-or-Demolition-of-Robot
# question screenshots

# https://leetcode.com/discuss/interview-question/2066692/Amazon-OA
'''
1.Demolition robot
Determine the min distance required for the robot to remove the obstacle
Input is given as a 2D array which consists of 0, 1 and 9
9 is the obstacle, can pass through 1 and cannot pass through 0
Robot can move top, left, right and bottom

Input: [[1,0,0],[1,0,0],[1,9,1]]
output: 3

i don't exactly remember the second one, it was like a Math tagged 1D dp problem
Solved 1st one with all test cases passed and attempted second one using recursion but TLE for many test cases
'''
