# RELATED LEETCODE QUESTION : 1383. Maximum Performance of a Team
'''
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

 

Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation: 
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72
 

Constraints:

1 <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
'''

###############################################################################################
# HEAP
# TC: O(N log N + N log k)
# SC: O(N + k)

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        candidates = zip(efficiency, speed)
        candidates = sorted(candidates, key = lambda t:t[0], reverse = True)
        
        speed_heap = []
        speed_sum = 0
        perf = 0
        
        for curr_efficiency, curr_speed in candidates:
            if len(speed_heap) > k - 1:
                speed_sum -= heapq.heappop(speed_heap)
            heapq.heappush(speed_heap, curr_speed)
            
            speed_sum += curr_speed
            perf = max(perf, speed_sum * curr_efficiency)
        
        # to prevent overflow of output
        modulo = 10 ** 9 + 7    
        return perf % modulo

       
 ####################################################################################################
 #GOOGLE QUESTION
'''
You have n items, cost is c(i) and delivery cost is d(i). 
If customer orders more than one item, then they get it for the minimum delivery cost. 
How do you find the maximum amount of money you can make after delivering m items? 

I know this is a knapsack problem, but I just can't find a way to solve it. 
And I want to make sure I am able to solve these problems for future interviews.

For e.g.
cost and delivery cost respectively (first column being cost, second being delivery cost):
Item 1: 7, 10
Item 2: 4, 15
Item3: 8, 1

m = 2
Input format (java): int n, int m, int[][] arr where n is the total number of items, 
m is the maximum number of items you can deliver, 
arr has each row with first element being cost, second being delivery cost.

Output: 31 (You choose the first two items because if you chose the 3rd item, 
the delivery cost for 2 items would be 1 + 1 (since 1 is the mimimum delivery cost) so you would end up with 23 + 2 = 25.
'''

####################################################################################################
# https://leetcode.com/discuss/interview-question/889942/any-idea-how-to-solve-this-problem-i-just-bombed-it-in-an-interview
# My solution with priority_queue in Python

import heapq
def solve(n, cost, delivery, m):
    orders = sorted(zip(delivery, cost), reverse=True)

    pq = []
    minRate = float('inf')
    sumCost = 0
    res = 0
    for i in range(n):
        d, c = orders[i]
        heapq.heappush(pq, (d, c))
        minRate = min(minRate, d)
        sumCost += c
        if len(pq) > m:
            minRate, mc = heapq.heappop(pq)
            sumCost -= mc
        res = max(res, (minRate*len(pq)) + sumCost)
    print(res) # prints 31 with provided input

'''
n = 3
cost = [7,4,8]
delivery = [10,15,1]
m = 2
solve(n, cost, delivery, m)
'''
####################################################################################################
