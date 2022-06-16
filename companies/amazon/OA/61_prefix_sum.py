# https://leetcode.com/discuss/interview-question/2118602/Amazon-OA
# https://leetcode.com/discuss/interview-question/2034486/Prefix-Sum-Amazon-OA
'''
I got the same question as:
https://leetcode.com/discuss/interview-question/2034486/Prefix-Sum-Amazon-OA

Does anyone have a better solution to this than O(n*m) as it passed only half of the test cases.

Appeared for Amazon OA recently, for internship role. This was the question
Given an Array contaning N integers find the prefix of the M times.
Example N=3
M=2
arr= 1 2 3
O/P-> 1 4 10
N=5
M=3
Arr= 1 2 3 4 5
O/P= 1 5 15 35 70
While converting to prefix sums, do the operation modulo 10^9 +7.
1<=N<=1000
1<=M,arr[i]<=10^9

I could pass only half the TCs. Remaning Time Limit Exceeding. how to solve it
'''
