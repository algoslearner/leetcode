'''
Given an array of integers greater than zero, f
ind if it is possible to split it in two (without reordering the elements), 
such that the sum of the two resulting arrays is the same. 

Print the resulting arrays 
'''

#####ASSUMPTION####
# Please note that the problem specifically targets subarrays that are contiguous 
# (i.e., occupy consecutive positions) and inherently maintains the order of elements.

#####################
# SOLUTION 1: TC: O(n2)
'''
A simple solution is to iterate the array and 
calculate the sum of the left and right subarray for each array element. 
'''
# Partition the list into two sublists with the same sum
def partition(A):
 
    # do for each element in the list
    for i in range(len(A)):
        left_sum = 0
        for j in range(i):
            left_sum += A[j]
 
        right_sum = 0
        for j in range(i, len(A)):
            right_sum += A[j]
 
        # if the sum of `A[0…i-1]` is equal to `A[i, n-1]`
        if left_sum == right_sum:
            return i
 
    # invalid input
    return -1
 
####################
# SOLUTION 2: TC: O(n), SC: O(1)
'''
The idea is to preprocess the array and calculate the sum of all array elements.

Then for each array element, we can calculate its right sum in O(1) time by using the following formula:
sum of right subarray = total sum – sum of elements so far
'''

# Partition the list into two sublists with the same sum
def partition(A):
 
    # calculate the sum of all list elements
    total_sum = sum(A)
 
    # variable to maintain the sum of processed elements
    sum_so_far = 0
 
    # do for each element in the list
    for i in range(len(A)):
 
        # if the sum of `A[0…i-1]` is equal to `A[i, n-1]`
        if sum_so_far == total_sum - sum_so_far:
            return i
 
        # update `sum_so_far` by including the value of the current element
        sum_so_far += A[i]
 
    return -1
 
 
if __name__ == '__main__':
    A = [6, -4, -3, 2, 3]
 
    # get index `i` that points to the starting of the second sublist
    i = partition(A)
 
    if i != -1:
        print(A[:i])        # print the first sublist, `A[0, i-1]`
        print(A[i:])        # print the second sublist, `A[i, len(A))`
    else:
        print("The list can't be partitioned")

      
 #########
 # Time : O(nk)
# Space: O(n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2
        
        for i in range(len(nums)):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False
