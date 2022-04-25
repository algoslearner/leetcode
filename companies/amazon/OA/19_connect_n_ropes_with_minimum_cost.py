# https://leetcode.com/discuss/interview-question/1475105/Amazon-OA
'''
I gave Amazon OA today on Hackerrank platform. There were two questions to be done in 105 min followed by a work-performance evaluation I believe. Could be related to Amazon leadership principles.

1. Min cost to join ropes of given lengths
2. Similar to BFS in a matrix.
3. Coding approach and Time complexity discussion for (1)
4. Coding approach and Time complexity discussion for (2)
Solved both.
How much time generally it takes for the recruiters to reach back after the OA?
'''

# https://www.gohired.in/2014/08/19/connect-n-ropes-with-minimum-cost/
'''
Connect n ropes: There are given n ropes of different lengths, we need to connect these ropes into one rope. 
The cost to connect two ropes is equal to sum of their lengths. We need to connect the ropes with minimum cost.

For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all ropes have connected.

Diff ways to connect

1) As it is… count = 4+3 = 7 , count = 7(previous)+ 7+2 = 16 , count = 16(previous)+9+6 =31.
2) Longest first
Array = 6,4,3,2
count = 6+4 =10 , count = 10+10+3=23 , count = 23+23+2 =48.

From above discussion we can understand that lengths of the ropes which are picked first are included more than once in total cost, 
hence we can say that choosing smallest ropes first will give optimal solution.
'''
