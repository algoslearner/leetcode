'''
The cost of stock on each day is given in an integer array arr[]. Find a pair of days in which  buying and selling the stock on those days makes you maximum profit.
Note: There may be multiple possible solutions. Return any correct solution.
Signature
int[] bestDaysToBuyAndSell(int[] arr)
Input
integer array arr of length N where index i is the day and Ai is the stock price corresponding to that day
2 ≤ N ≤ 106
0 ≤ Ai ≤ 1000
Output
One possible pair of days that maximizes profit returned as an array of integers
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Example 1:
Input:
arr = [100, 180, 260, 310, 40, 535, 695]
Output:
[4, 6]
Explanation:
We can buy stock on day 4 and sell it on day 6, which will give us maximum profit of 655.
Example 2:
Input:
arr = [4,2,2,2,4]
Output:
[3,4]
Explanation:
There are multiple possible solutions. If we buy on day 1 and sell on day 4, we would make maximum profit of 2. That is also true of (2, 4) and (3,4)
'''

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def bestDaysToBuyAndSell(arr):
  # Write your code here
  output = [0,0]
  
  minprice = math.inf
  maxprice = -math.inf
  for i in range(len(arr)):
    if i == 0 or arr[i] < minprice:
      minprice = arr[i]
      output[0] = i
    elif arr[i] > maxprice:
      maxprice = arr[i]
      output[1] = i

  return output
