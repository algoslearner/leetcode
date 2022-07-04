# https://leetcode.com/problems/paint-house/
'''
256. Paint House

There is a row of n houses, where each house can be painted one of three colors: red, blue, or green. 
The cost of painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by an n x 3 cost matrix costs.

For example, costs[0][0] is the cost of painting house 0 with the color red; 
costs[1][2] is the cost of painting house 1 with color green, and so on...

Return the minimum cost to paint all houses.

 

Example 1:

Input: costs = [[17,2,17],[16,16,5],[14,3,19]]
Output: 10
Explanation: Paint house 0 into blue, paint house 1 into green, paint house 2 into blue.
Minimum cost: 2 + 5 + 3 = 10.
Example 2:

Input: costs = [[7,6,2]]
Output: 2
 

Constraints:

costs.length == n
costs[i].length == 3
1 <= n <= 100
1 <= costs[i][j] <= 20
'''

###############################################################################################
# Brute force
# TC: O(2^n)
# SC: O(n)

def minCost(self, costs):
    """
    :type costs: List[List[int]]
    :rtype: int
    """

    def paint_cost(n, color):
        total_cost = costs[n][color]
        if n == len(costs) - 1:
            pass
        elif color == 0: # Red
            total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
        elif color == 1: # Green
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
        else: # Blue
            total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
        return total_cost

    if costs == []:
        return 0
    return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))

###############################################################################################
# DP
# TC: O(N)
# SC: O(1)
# https://leetcode.com/problems/paint-house/solution/

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0: return 0

        previous_row = costs[-1]
        for n in reversed(range(len(costs) - 1)):

            current_row = copy.deepcopy(costs[n])
            # Total cost of painting nth house red?
            current_row[0] += min(previous_row[1], previous_row[2])
            # Total cost of painting nth house green?
            current_row[1] += min(previous_row[0], previous_row[2])
            # Total cost of painting nth house blue?
            current_row[2] += min(previous_row[0], previous_row[1])
            previous_row = current_row

        return min(previous_row)
