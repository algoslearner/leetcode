# https://leetcode.com/discuss/interview-question/1985355/Amazon-OA-SDE2
'''
1. given an array consisting of only 1 and -1, return the max length of the subarray such that the product of all elements in said subarray is 1 https://leetcode.com/discuss/interview-question/1655441/amazon-oa
2. given an array and an integer k, return the number of subarrays such that the difference between its max value and its min values is no more than k https://leetcode.com/discuss/interview-question/1904966/Amazon-orOAorset-7
'''

####################################################################################################
'''
q2 is variation of https://leetcode.com/problems/sliding-window-maximum/
Can be solved in O(n) with sliding window.
Since difference will increase as right pointer goes right, and decrease as left pointer goes right,
therefore, for each selected right pointer, we can locate the left-most left pointer so that difference is within k, then (right - left) is the number of satisfying subarrays end with rightPointer, add this number to count.
Maintain 2 Deque, one for window max and one for window min, each element will be offered at most twice and polled at most twice, thus O(4n) = O(n).

The idea/solution u are talking about is the same as the one in the comment section, right?https://leetcode.com/discuss/interview-question/1994481/Need-Help!-AMAZON-OA
'''
