# given an array and an integer k, return the number of subarrays such that the difference between its max value and its min values is no more than k 
# https://leetcode.com/discuss/interview-question/1904966/Amazon-orOAorset-7

'''
#################################################
1. A question about Amazon student badges but ultimately the problem was given an arr of -1 or 1, return the maximum subarray length with a product of 1.
The array is of size 2 and above and only contains -1 and 1
e.g arr = [-1,-1,1,1,-1], return 4, since index 0 to 3 have the max length with product equal to 1

I tried to use a sliding window but only passed 4/13 cases. there was somthing i had to fix in the logic for the case arr = [ -1,-1,-1,-1,-1, 1]

#################################################
2. Given an array containing only 0 and 1 as its elements. 
We have to sort the array in such a manner that all the ones are grouped together and all the zeros are grouped together. 
The group of ones can be either at the start of the array or at the end of the array. 
The constraint while sorting is that every one/zero can be swapped only with its adjacent zero/one. 
Find the minimum number of moves to sort the array as per the description.

Example:
input array ={0,1,0,1}
Final array = {0,0,1,1}
Minimum moves = 1 (1 at index 1 is swapped with 0 at index 2)

input array = { 1101}
Final array - {1110}
Minimum moves = 1 {1 at index 2 is swapped with index 3}

I passed all test cases on this one 13/13.

I ran a sliding window to check number of swaps if the elements on the left should be 0s before 1s, and at each 0 found by right index, I found the number of swaps needed
repeated the same above for the case if the elements on the left should be 1s before 0s,
returned the minimum of both operations.

Do I have even a miniscule chance of moving forward

Update: I think was rejected 😭😭😭
'''
