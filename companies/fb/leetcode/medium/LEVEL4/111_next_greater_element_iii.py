'''
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 231 - 1
'''

# https://leetcode.com/problems/next-greater-element-iii/discuss/1146065/Python-100-less-memory-Explained-with-example
#################################################################
'''
Explaination

Steps:

Create a list of numbers so that each digit can be accessed seperately.
Loop :
Find decreasing sequence in the given no. Store the index of the no to be swapped.
If index = -1, that means the given no is in decreasing sequence and thus, there is no possible combination that could yield the result.
Loop :
Find the no in the right sequence that is just greater than the no to be swapped.
Swap the nos.
Since the right part of the sequence found in Step - 1 will always be a decreasing sequence, reverse the sequence to get the smallest possible no.
Store the result.
Check the result for 32-bit integer and return it.
For eg. : Let n = 14951

Steps:

List = [1,4,9,5,1]
Decreasing sequence : 951 and index = 3 (i.e. index of digit 4).
no just greater than 4 in the decreasing seq = 5
Swap : List = [1,5,9,4,1]
Reverse the decreasing sequence i.e. [9,4,1] to [1,4,9]
result = 15149
Since result is a 32-bit int, return the result.
'''

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
		#Step - 1
        nums = list(map(int, str(n)))
        
		#Step - 2
        indx = len(nums) - 2
        while indx >= 0 and nums[indx] >= nums[indx + 1]:
            indx -= 1
        if indx == -1:
            return -1               #If no is a decreasing sequence (eg. 5421)
        
		#Step - 3
        indx2 = len(nums) - 1
        while nums[indx2] <= nums[indx]:
            indx2 -= 1
        
		#Step - 4
        nums[indx], nums[indx2] = nums[indx2], nums[indx]
		
		#Step - 5
        nums[indx+1 :] = reversed(nums[indx+1 :])
        
		#Step - 6
        res = ''
        for n in nums:
            res += str(n)
        res = int(res)
        
		#Step - 7
        return res if res <= 2 ** 31 - 1 else -1

'''
This is the Next Permutation problem - https://leetcode.com/problems/next-permutation/
This is the best explanation that I've seen - https://www.youtube.com/results?search_query=back+to+back+next+permutation
'''
