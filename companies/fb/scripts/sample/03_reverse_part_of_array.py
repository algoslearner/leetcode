'''
In a given array, rotate a part of the array for which the index is given

or 

Given a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) reverse the order of the elements

'''

def reversePartOfArray(nums, left, right):
	print(nums)
	while(left < right):
		tmp = nums[left]
		nums[left] = nums[right]
		nums[right] = tmp
		left += 1
		right -= 1
	print(nums)

# TC: O(n)
# SC: O(1)

# tests
nums = [1,2,3,4, 5, 6, 7]
reversePartOfArray(nums, 2, 5)

# output
'''
[1, 2, 3, 4, 5, 6, 7]
[1, 2, 6, 5, 4, 3, 7]
'''


