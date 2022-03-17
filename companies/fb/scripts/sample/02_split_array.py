'''
Position: Production Engineer

You're given an array made up of positive integers. 
Split the given array into two smaller arrays where the sums of each smaller array are equal. 
Print out the two smaller arrays.

eg.
[1,2,1,1,3] -> [1,2,1] & [1,3]
[1,1,1,1,1,5] -> [1,1,1,1,1] & [5]
[5,2,3] -> [5] & [2,3]

-> had to ask for clarification: print any arbitary error message if the given array isn't splitable.
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

      
######################################################################################################
# Two pointers
# Time : O(n)
# Space: O(1)

def printSplitArray(nums):
	if sum(nums) % 2 != 0:
		print("Array cannot be split into two equal subarrays")
		return
		
	j = len(nums) - 1
	leftsum = 0
	rightsum = 0
	found = 0
	target = sum(nums) // 2
	for i in range(len(nums)):
		leftsum += nums[i]
		
		while leftsum > rightsum and j > 0 and j < len(nums):
			rightsum += nums[j]
			j -= 1
		
		if leftsum == rightsum == target:
			pivot = i+1
			print("Equal split")
			print(nums[:pivot])
			print(nums[pivot:len(nums)])
			found = 1
			break
	
	if found == 0:
		print("Error: array cannot be split into same subarrays")

# tests
# nums = [1,2,1,1,3]
# nums = [1,1,1,1,1,5]
nums = [5,2,3]

# nums = [1]
# nums = []
# nums = [3,4]
printSplitArray(nums)
