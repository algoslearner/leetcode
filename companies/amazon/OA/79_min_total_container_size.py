# https://leetcode.com/discuss/interview-question/977057/Amazon-or-OA
'''
Here is the problem: https://aonecode.com/Amazon-Online-Assessment-Minimum-Total-Container-Size

My intuition is to use dp and the bottom-up approach that I came up with is to have dp[m][n] = answer for subarray from index 0...m on the nth day.

As I thought more about the implementation, it seems that it would be O(m * m * n). Is there are better way to do this?

in the given problem you need to find a sum of containers. For the problem that you provided we need to find a min container size which will fit all items within D days
'''
