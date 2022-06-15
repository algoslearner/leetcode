# 
'''
Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take the step. 
Implement a method to calculate the minimum fee required to reach the top of the staircase (beyond the top-most step). 

At every step, you have an option to take either 1 step, 2 steps, or 3 steps. 
You should assume that you are standing at the first step.

Example 1:

Number of stairs (n) : 6
Fee: {1,2,5,2,1,2}
Output: 3
Explanation: Starting from index '0', we can reach the top through: 0->3->top
The total fee we have to pay will be (1+2).
Example 2:

Number of stairs (n): 4
Fee: {2,3,4,5}
Output: 5
Explanation: Starting from index '0', we can reach the top through: 0->1->top
The total fee we have to pay will be (2+3).
'''

###############################################################################################################################
# recursion
# TC: O(3^n)
# SC: O(n)

def find_min_fee(fee):
  return find_min_fee_recursive(fee, 0)


def find_min_fee_recursive(fee, currentIndex):
  n = len(fee)
  if currentIndex > n - 1:
    return 0

  # if we take 1 step, we are left with 'n-1' steps;
  take1Step = find_min_fee_recursive(fee, currentIndex + 1)
  # similarly, if we took 2 steps, we are left with 'n-2' steps;
  take2Step = find_min_fee_recursive(fee, currentIndex + 2)
  # if we took 3 steps, we are left with 'n-3' steps;
  take3Step = find_min_fee_recursive(fee, currentIndex + 3)

  _min = min(take1Step, take2Step, take3Step)

  return _min + fee[currentIndex]


def main():
  print(find_min_fee([1, 2, 5, 2, 1, 2]))
  print(find_min_fee([2, 3, 4, 5]))


main()

###############################################################################################################################
# top down dp
# TC: O(n)
# SC: O(n)

def find_min_fee(fee):
  dp = [0 for x in range(len(fee))]
  return find_min_fee_recursive(dp, fee, 0)


def find_min_fee_recursive(dp, fee, currentIndex):
  n = len(fee)
  if currentIndex > n-1:
    return 0

  if dp[currentIndex] == 0:
    # if we take 1 step, we are left with 'n-1' steps
    take1Step = find_min_fee_recursive(dp, fee, currentIndex + 1)
    # similarly, if we took 2 steps, we are left with 'n-2' steps
    take2Step = find_min_fee_recursive(dp, fee, currentIndex + 2)
    # if we took 3 steps, we are left with 'n-3' steps
    take3Step = find_min_fee_recursive(dp, fee, currentIndex + 3)

    dp[currentIndex] = fee[currentIndex] + \
                       min(take1Step, take2Step, take3Step)

  return dp[currentIndex]


def main():

  print(find_min_fee([1, 2, 5, 2, 1, 2]))
  print(find_min_fee([2, 3, 4, 5]))


main()

###############################################################################################################################
# bottom up dp
# TC: O(n)
# SC: O(n)

def find_min_fee(fee):
  n = len(fee)
  dp = [0 for x in range(n+1)]  # +1 to handle the 0th step
  dp[0] = 0  # if there are no steps, we don't have to pay any fee
  dp[1] = fee[0]  # only one step, so we have to pay its fee
  # for 2 steps, since we start from the first step, so we have to pay its fee
  # and from the first step we can reach the top by taking two steps, so
  # we don't have to pay any other fee.
  dp[2] = fee[0]

  # please note that dp[] has one extra element to handle the 0th step
  for i in range(2, n):
    dp[i + 1] = min(fee[i] + dp[i], 
                    fee[i - 1] + dp[i - 1], 
                    fee[i - 2] + dp[i - 2])

  return dp[n]


def main():

  print(find_min_fee([1, 2, 5, 2, 1, 2]))
  print(find_min_fee([2, 3, 4, 5]))


main()
